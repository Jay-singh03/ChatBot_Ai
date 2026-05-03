<<<<<<< HEAD
# ChatBot_AI

## Overview

ChatBot_AI is a Flask-based chatbot application with OpenAI integration, user authentication, and an admin dashboard. It includes a web interface for chatting and voice input support.

## Repository Structure

- `backend/app.py` - Flask web API for chat, user authentication, and admin dashboard
- `backend/requirements.txt` - Python dependencies
- `frontend/templates/index.html` - Main chat interface with login
- `frontend/templates/admin.html` - Admin dashboard for viewing chat history
- `frontend/static/script.js` - Frontend JavaScript for chat and login functionality
- `frontend/static/style.css` - CSS styling for the web interface
- `Procfile` - For Heroku deployment

## Prerequisites

Install Python 3.8+ and the required packages.

```bash
pip install -r backend/requirements.txt
```

## Setup

1. Set environment variables:
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `SECRET_KEY`: A random secret key for Flask sessions

2. Run the application:

```bash
python backend/app.py
```

The application starts at `http://127.0.0.1:5000`.

## Features

- User login/logout
- Chat with OpenAI GPT model
- Voice input support (where available)
- Email collection from chat messages
- Admin dashboard for viewing chat history
- SQLite database for persistence

## API Endpoints

- `GET /` - Home page with login/chat interface
- `POST /login` - User login
- `POST /logout` - User logout
- `POST /chat` - Send chat message
- `GET /history` - Get chat history (JSON)
- `GET /admin` - Admin dashboard (requires login)

## Database

Uses SQLite (`chatbot.db`) with tables for ChatHistory, UserEmail, and User.

## Deployment

For Heroku, use the provided `Procfile`.

## License

This project is provided under the terms of the included `LICENSE` file.
=======
# ChatBot-Ai
>>>>>>> 1ae1fd3bf1e08946be4c8ac3858e23ecf76f403a
