# ChatGPT TTS Client

its great

# Compiling/Running

## Compiling

You can't really compile since python is an interpreted language...

## Running

type `python -m venv venv` then open the activate script in the venv folder which could be venv\Scripts\activate or venv\bin\activate, type `pip install -r requirements.txt` and then type `python main.py` or `python3 main.py` something like that.

# Notes

Make sure that you change the API key in the python file (it's called openai.api_key)

This works better on windows or macOS because the tts voice is easier to understand.

This app uses microphone input to input the message, if you want to enable this change message_input to audio (in the code)
