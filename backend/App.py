from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import openai
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
import os

openai.api_key = os.getenv("OPENAI_API_KEY")  # Set your OpenAI API key in environment variables

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')

app.secret_key = os.getenv("SECRET_KEY", "default_secret_key")  # Change this to a random secret key

# Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chatbot.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)

# Models
class ChatHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_message = db.Column(db.String(500), nullable=False)
    bot_response = db.Column(db.String(500), nullable=False)

class UserEmail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(10), nullable=False)  # admin / student

# Create DB
with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Chatbot logic
def chatbot_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": user_input}]
        )
        return response['choices'][0]['message']['content']
    except:
        return "AI is currently unavailable."

# ✅ HOME ROUTE (IMPORTANT FIX)
@app.route("/")
def home():
    return render_template("index.html")

# Chat API (POST)
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "Message is empty"}), 400

    # Email detection
    if "@" in user_message and "." in user_message:
        existing_email = UserEmail.query.filter_by(email=user_message).first()
        if not existing_email:
            new_email = UserEmail(email=user_message)
            db.session.add(new_email)
            db.session.commit()
        return jsonify({"reply": "Thank you! Your email has been saved."})

    # Chat response
    response = chatbot_response(user_message)

    # Save chat
    new_chat = ChatHistory(user_message=user_message, bot_response=response)
    db.session.add(new_chat)
    db.session.commit()

    return jsonify({"reply": response})

# Login route
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()

    if user and bcrypt.check_password_hash(user.password, data['password']):
        login_user(user)
        return jsonify({"message": "Login successful", "role": user.role})
    
    return jsonify({"message": "Invalid credentials"})

# Logout route
@app.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out successfully"})

# Get chat history
@app.route("/history", methods=["GET"])
def get_chat_history():
    chats = ChatHistory.query.all()
    chat_data = [{"user": chat.user_message, "bot": chat.bot_response} for chat in chats]
    return jsonify({"history": chat_data})

# Admin dashboard
@app.route("/admin")
@login_required
def admin():
    if current_user.role != 'admin':
        return "Access denied", 403
    chats = ChatHistory.query.all()
    return render_template("admin.html", chats=chats)

if __name__ == "__main__":
    app.run(debug=True)