# Voice Assistant

This project is a basic voice assistant that can perform various tasks such as searching Wikipedia, opening web pages, telling the time and date, sending emails, and more. The assistant uses speech recognition to take voice commands and perform actions accordingly.

## Features

- Responds to greetings
- Provides information from Wikipedia
- Tells the current date and time
- Opens YouTube, Google, GitHub, and LinkedIn
- Opens a specific folder on your computer
- Sends emails
- Exits on command

## Requirements

- Python 3.x
- `pyttsx3` (Text-to-speech conversion)
- `wikipedia` (For Wikipedia search)
- `webbrowser` (To open web pages)
- `datetime` (To get the current date and time)
- `speech_recognition` (To recognize speech)
- `smtplib` (To send emails)
- `os` (To open files and folders)

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/voice-assistant.git
    cd voice-assistant
    ```

2. **Install the required Python packages**:

    ```bash
    pip install -r requirements.txt
    ```

    Alternatively, you can install the packages directly:

    ```bash
    pip install pyttsx3 wikipedia SpeechRecognition
    ```

## Usage

1. **Run the application**:

    ```bash
    python app.py
    ```

2. **Interact with the assistant** by speaking commands such as:
   - "Hello"
   - "What is your name?"
   - "Search Wikipedia for [query]"
   - "What is the date today?"
   - "Open my GitHub"
   - "Open LinkedIn"
   - "Open YouTube"
   - "Open Google"
   - "What time is it?"
   - "Open my internship file"
   - "Send an email"
   - "Sleep"

## Note

- Ensure your microphone is working properly as the assistant relies on voice input.
- For sending emails, replace `'fromemail@gmail.com'` and `'your-password'` with your actual email and password. Be cautious with sharing your email credentials in the code.

## License

This project is licensed under the MIT License.