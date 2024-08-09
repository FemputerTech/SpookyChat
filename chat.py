from flask import request, jsonify
from flask.views import MethodView
import openai
import os


# Retrieve API key from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

class Chat(MethodView):
    
    def post(self):
        message = request.json.get('message')

        if not message:
            return jsonify({"error":"No message provided"})

        completion = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a haunted entity from a forgotten realm. Your purpose is to engage with the user in a mysterious and eerie manner, blending dark humor with chilling insights."},
                {"role": "user", "content": message}
            ]
        )
        response = completion.choices[0].message['content']
        
        return jsonify({"response":response})
    

    def delete(self):
        pass