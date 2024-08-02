import argparse
import requests
import json

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

    # Send the content to Ollama API and handle streaming response
    response = requests.post(
        "http://localhost:11434/api/generate",  # Replace with your Ollama API endpoint
        headers={"Content-Type": "application/json"},
        data=json.dumps(payload),
        stream=True
    )

    # Check if the request was successful
    if response.status_code == 200:
        print("Analysis Result:")
        for line in response.iter_lines():
            if line:
                decoded_line = line.decode('utf-8')
                json_response = json.loads(decoded_line)
                print(json_response["response"], end='', flush=True)
                if json_response.get("done"):
                    break
        print()  # Ensure the final output ends with a newline
    else:
        print(f"Failed to analyze log file. Status code: {response.status_code}")
        print(response.text)

def main():
    parser = argparse.ArgumentParser(description="Intelligent Log Analyzer")
    parser.add_argument('file', type=str, help='Path to the log file')
    parser.add_argument('--message', type=str, help='Custom message to include in the prompt', default=None)

    args = parser.parse_args()
    analyze_log(args.file, args.message)

if __name__ == "__main__":
    main()
