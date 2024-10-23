# Prompt Generator

## Overview

Prompt Generator is a web application designed to help users create detailed system prompts for AI models. It leverages OpenAI's API to generate prompts based on user input and predefined meta prompts.

## Features

- Generate text or audio prompts for AI models.
- Choose from different OpenAI models for prompt generation.
- User-friendly interface built with Streamlit.

## Prerequisites

- Python 3.7 or higher
- OpenAI API key

## Installation

1. Clone the repository:

   ```
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

3. Set your OpenAI API key as an environment variable:

   ```
   export OPENAI_API_KEY='your-api-key'
   ```

## Usage

1. Run the application:

   ```
   streamlit run prompt-generator.py
   ```

2. Open your web browser and go to the URL provided by Streamlit.

3. Select the output format (Text or Audio prompt).

4. Choose the OpenAI model you want to use.

5. Enter the task, goal, or current prompt in the provided text area.

6. Click 'Generate' to create a prompt.

## Configuration

The application uses a configuration file `config.json` to store meta prompts for text and audio outputs. You can modify these prompts to suit your needs.

## License

This project is licensed under the MIT-0 License. See the LICENSE file for more details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.