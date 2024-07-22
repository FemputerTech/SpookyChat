"""
The application uses Flask to create a web interface and includes some modules:
- Index: Handles the main landing page

Environment Variables:
- API_KEY: Required for accessing OpenAI API

To run the application, execute this script.
"""
import os
import flask
from index import Index


# Initializes the Flask application
app = flask.Flask(__name__)


# URL routing for the main landing page
app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=['GET']
                 )


# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)