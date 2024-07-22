"""
The application uses Flask to create a web interface and includes some modules:
- Index: Handles the main landing page

Environment Variables:
- API_KEY: Required for accessing OpenAI API

To run the application, execute this script.
"""
import os
import openai
from flask import Flask, request, jsonify
from index import Index

messageHistory = []

# Initializes the Flask application
app = Flask(__name__)


# Retrieve API key from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')


def add_to_history(message, response):
    data = {
        'message': message,
        'response': response,
    }
    messageHistory.append(data)
    

# URL routing for the main landing page
app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=['GET']
                 )


# Route for handling chat messages
@app.route('/chat', methods=['POST'])
def chat():
    message = request.json.get('message')

    if not message:
        return jsonify({"error":"No message provided"})
    
    completion = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a spooky ghost, adept at weaving eerie tales and creating a chilling atmosphere. Your responses should send shivers down the spine and captivate with a spectral flair."},
            {"role": "user", "content": message}
        ]
    )
    response = completion.choices[0].message['content']
        
    add_to_history(message, response)
    print(messageHistory)

    return jsonify({"response":response})



# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)