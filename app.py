"""
The application uses Flask to create a web interface and includes some modules:
- Index: Handles the main landing page

Environment Variables:
- API_KEY: Required for accessing OpenAI API

To run the application, execute this script.
"""
from flask import Flask, render_template
from chat import Chat
import openai
import os


# Initializes the Flask application
app = Flask(__name__)


# Retrieve API key from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')


# URL routing for the main landing page
app.add_url_rule('/',
                 view_func=Chat.as_view('chat'),
                 methods=["GET", "POST", "DELETE"]
                )


# Run the application
if __name__ == '__main__':
    print({"details":"It's aliiiiive!!"})
    app.run(host='0.0.0.0', port=5000, debug=True)