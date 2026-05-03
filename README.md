<<<<<<< HEAD
# ChatBot_AI

## Overview

ChatBot_AI is a Python-based chatbot project that includes:
- a PyTorch model for intent classification
- a command-line chat interface
- a Flask REST API with SQLite storage for chat history and user emails
- basic NLTK preprocessing for tokenization, stemming, and bag-of-words feature extraction

## Repository Structure

- `App.py` - Flask web API for chat and chat history storage
- `train.py` - trains the chatbot model from intent patterns and saves `data.pth`
- `chat.py` - runs a CLI chatbot using the trained model
- `model.py` - defines the neural network architecture
- `nltk_utils.py` - tokenization, stemming, and bag-of-words utilities
- `jsonfile.py` - currently contains the intent dataset and should be renamed to `intents.json`

## Prerequisites

Install Python 3.8+ and the required packages.

```bash
pip install torch numpy nltk flask flask_sqlalchemy
```

If you are using a virtual environment, activate it first.

### NLTK Data

The project uses NLTK tokenization. Run this once if you have not downloaded the dataset:

```python
import nltk
nltk.download('punkt')
```

## Setup

1. Make sure the intent dataset file exists as `intents.json` in the project root.
   - If your repository currently has `jsonfile.py` containing JSON data, rename it:

```bash
ren jsonfile.py intents.json
```

2. Train the model:

```bash
python train.py
```

This creates `data.pth` in the project root.

## Usage

### Run the CLI chatbot

```bash
python chat.py
```

Then type messages. Enter `quit` to stop.

### Run the Flask API

```bash
python App.py
```

The API starts at `http://127.0.0.1:5000` with two endpoints:

- `POST /chat` - send JSON payload `{ "message": "..." }`
- `GET /history` - retrieve stored chat history

### Example request

```bash
curl -X POST http://127.0.0.1:5000/chat -H "Content-Type: application/json" -d '{"message":"hello"}'
```

## Database

`App.py` uses SQLite and stores data in `chatbot.db`.

Tables:
- `ChatHistory` - user messages and bot responses
- `UserEmail` - collected user emails

## Notes

- `train.py` uses a simple feedforward neural network with one hidden layer.
- `chat.py` loads the saved `data.pth` file and answers based on intent confidence.
- `App.py` currently has a hardcoded response dictionary and stores history for audit/debug.

## License

This project is provided under the terms of the included `LICENSE` file.
=======
# ChatBot-Ai
>>>>>>> 1ae1fd3bf1e08946be4c8ac3858e23ecf76f403a
