import argparse
import requests
import json
import threading
import time
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def analyze_log(file_path, custom_message=None):
    # Default prompt message
    default_message = "Hi. Please, take a look at this log content and find error lines if any. If possible, give some clues on how to resolve these issues."
    prompt_message = custom_message if custom_message else default_message

    # Read the log file
    with open(file_path, 'r') as file:
        log_content = file.read()

    # Prepare the data to be sent to the Ollama API
    payload = {
        "model": "mistral",
        "prompt": f"{prompt_message}\n\n{log_content}"
    }

    # Function to display a loading animation
    def loading_animation(stop_event):
        while not stop_event.is_set():
            for char in "|/-\\":
                print(Fore.YELLOW + f'\rLoading {char}', end='', flush=True)
                time.sleep(0.1)
                if stop_event.is_set():
                    break
        print('\r', end='', flush=True)  # Clear the loading line

    # Event to signal the loading animation to stop
    stop_event = threading.Event()

    # Start the loading animation in a separate thread
    loader_thread = threading.Thread(target=loading_animation, args=(stop_event,))
    loader_thread.start()

    # Send the content to Ollama API and handle streaming response
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",  # Replace with your Ollama API endpoint
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload),
            stream=True
        )

        # Check if the request was successful
        if response.status_code == 200:
            stop_event.set()
            loader_thread.join()
            print(Fore.GREEN + "\nAnalysis Result:")
            for line in response.iter_lines():
                if line:
                    decoded_line = line.decode('utf-8')
                    json_response = json.loads(decoded_line)
                    print(Fore.CYAN + json_response["response"], end='', flush=True)
                    if json_response.get("done"):
                        break
            print()  # Ensure the final output ends with a newline
        else:
            stop_event.set()
            loader_thread.join()
            print(Fore.RED + f"\nFailed to analyze log file. Status code: {response.status_code}")
            print(Fore.RED + response.text)
    except Exception as e:
        stop_event.set()
        loader_thread.join()
        print(Fore.RED + f"\nAn error occurred: {str(e)}")
    finally:
        # Ensure the loading animation stops in case of any unexpected errors
        stop_event.set()
        loader_thread.join()

def main():
    parser = argparse.ArgumentParser(description="Intelligent Log Analyzer")
    parser.add_argument('file', type=str, help='Path to the log file')
    parser.add_argument('--message', type=str, help='Custom message to include in the prompt', default=None)

    args = parser.parse_args()
    analyze_log(args.file, args.message)

if __name__ == "__main__":
    main()
