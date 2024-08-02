# Intelligent Log Analyzer

This project is a command-line tool for analyzing log files using the Ollama API with the Mistral model. The tool reads the content of a log file, sends it to the Ollama API for analysis, and displays the results in real-time. The analysis focuses on identifying error lines and providing possible solutions.

## Features

- **Command-Line Interface**: Easily analyze log files from the command line.
- **Streaming Response Handling**: Processes and displays API responses in real-time.
- **Customizable Prompts**: Optionally provide a custom message to be included in the analysis prompt.
- **Colored Output**: Enhanced readability with colored terminal output.
- **Loading Animation**: Visual feedback during the request processing.

## Prerequisites

- Python 3.x
- `requests` library
- `colorama` library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/koladev/smartlog.git
   cd smartlog
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required libraries:
   ```bash
   pip install requests colorama
   ```

## Usage

To use the tool, run the `smartlog.py` script with the path to your log file and optionally a custom message:

```bash
python smartlog.py /path/to/your/logfile.log
```

To include a custom message in the prompt:

```bash
python smartlog.py /path/to/your/logfile.log --message "Please analyze this log and summarize the critical points."
```

### Example

```bash
python smartlog.py logs/system.log --message "Check this log for errors and suggest fixes."
```

## How It Works

1. **Reading the Log File**: The content of the specified log file is read.
2. **Preparing the Prompt**: A default prompt message is used unless a custom message is provided.
3. **Sending to Ollama API**: The log content is sent to the Ollama API for analysis.
4. **Handling the Response**: The API's streaming response is processed and displayed in real-time.
5. **Colored Output**: The results are displayed with colored text for better readability.
6. **Loading Animation**: A loading spinner provides visual feedback while the request is processed.

## Dependencies

- `requests`
- `colorama`

## License

This project is licensed under the MIT License.

## Acknowledgments

- [Ollama API](https://ollama.com/)
- [Colorama](https://pypi.org/project/colorama/)

## Contact

For any questions or feedback, please contact [koladev32@gmail.com](mailto:koladev32@gmail.com).

---

This README provides an overview of the project, installation instructions, usage examples, and other relevant information to get started with the Intelligent Log Analyzer.
