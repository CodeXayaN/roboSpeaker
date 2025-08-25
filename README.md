# RoboSpeaker 🗣️

RoboSpeaker is a simple Python-based text-to-speech program that uses Windows PowerShell's built-in `System.Speech` library to convert text into speech.

## Features
- Converts any text input into speech.
- Runs directly in the terminal.
- Exits gracefully when the user enters `q`.
- Works on Windows without requiring external libraries.

## Requirements
- **Windows OS** (because it uses PowerShell).
- **Python 3.x** installed on your system.

## How it Works
- The script takes user input.
- It passes the input text to a PowerShell command that uses `System.Speech.Synthesis.SpeechSynthesizer`.
- PowerShell then speaks out the text.
- Typing `q` will exit the program after saying *"bye bye friend"*.

## Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/robospeaker.git
   cd robospeaker
