# CodeGenie

**CodeGenie** is an advanced AI-powered tool designed to streamline Python coding tasks. This application allows you to generate Python code based on user prompts, execute it, and automatically handle debugging, all with the power of artificial intelligence.

## Features

- **Dynamic Code Generation**: Generate Python code based on user-provided prompts.
- **Automated Execution**: Execute the generated Python code in a secure environment.
- **Intelligent Debugging**: Automatically fix errors and handle missing modules.
- **Interactive Input Handling**: Provide values for function parameters interactively.
- **Retry Mechanism**: Multiple attempts to ensure successful code execution.

## Demo

Check out the demo of the application: [CodeGenie](https://codegenieai.streamlit.app/)


## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/RiteshGenAI/CodeGenie.git
    ```
2. **Navigate to the project directory:**
    ```bash
    cd CodeGenie
    ```
3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the application:**
    ```bash
    streamlit run .\src\app.py
    ```
2. **Access the application in your web browser** at `http://localhost:8501`.

3. **Enter your Python code prompt** in the text area to generate code.

4. **Provide values for any input parameters** if required.

5. **Execute the generated code** and view the results or errors.

## Configuration

- **GROQ_API_KEY**: Set your API key for the Groq service in the `.env` file to enable code generation and fixing. Replace the placeholder with your actual API key.

## Contributing

1. **Fork the repository** to your GitHub account.
2. **Create a new branch** for your feature or bug fix.
3. **Make your changes** and test thoroughly.
4. **Submit a pull request** with a description of your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
