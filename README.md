# Voice-Activated Personal Assistant

## Overview

The **Voice-Activated Personal Assistant** is a Python-based application that uses voice recognition to perform various tasks such as playing music, reading PDF files, providing weather updates, and controlling hardware components through Arduino. This project showcases the integration of speech recognition, text-to-speech, and serial communication to create a functional voice assistant.

## Features

- **Voice Recognition**: Listens for commands and responds accordingly.
- **Text-to-Speech**: Converts text responses into spoken words using the `pyttsx3` library.
- **Weather Updates**: Fetches current weather information using the OpenWeatherMap API.
- **PDF Reading**: Reads and vocalizes the contents of PDF files.
- **Music Playback**: Plays MP3 files using the `pygame` library.
- **Arduino Integration**: Controls an Arduino board to perform tasks such as turning LEDs on/off and moving a robotic arm.

## Requirements

Make sure you have the following libraries installed:

- `pyttsx3`
- `speech_recognition`
- `pygame`
- `PyPDF2`
- `requests`
- `pyserial`

You can install the required libraries using pip:

```bash
pip install pyttsx3 SpeechRecognition pygame PyPDF2 requests pyserial
```


## Getting Started

### Hardware Setup

#### Arduino Setup:

1. Connect your Arduino board to your computer.
2. Load the necessary code onto your Arduino to handle the commands sent from the Python script.

#### Wiring:

- Connect any LEDs or motors as needed for your project.

### Software Setup

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Anitha-Chava/voice-activated-personal-assistant.git
   cd voice-activated-personal-assistant
   ```
2. Open the main Python file and set the correct serial port for your Arduino (e.g., COM8 on Windows).
3. Ensure you have an internet connection for API calls to DuckDuckGo and OpenWeatherMap.

### Running the Assistant

```bash
python assistant.py
```
## Commands

You can use the following commands with your voice:

## Basic Commands:

"What time is it?"
"How are you?"
"Search for [query]."
"Weather in [city]."
"Read PDF."
"Play [song name]."
Note : pdf file, song files paths can change according to your system

## Arduino Commands:
1. "Shake hand."
2. "Walk."
3. "Turn left."
4. "Turn right."
5. "Move back."

## Code Explanation

- speak(text): Converts text to speech using the pyttsx3 library.
- take_command(idle_mode): Listens for voice input and recognizes commands.
- play_mp3(file_path): Plays an MP3 file using the pygame mixer.
- read_pdf(filepath): Reads and vocalizes the text from a specified PDF file.
- get_weather(city): Retrieves weather information from the OpenWeatherMap API.
- listen_for_wakeup_word(): Listens for a specific wake-up word to activate the assistant.

## Contributions

Feel free to contribute by forking this repository and submitting pull requests. Suggestions and improvements are welcome!

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

- pyttsx3 for text-to-speech functionality.
- SpeechRecognition for voice command recognition.
- pygame for audio playback.
- PyPDF2 for PDF reading capabilities.
- requests for making HTTP requests to APIs.
- Arduino for hardware integration.

