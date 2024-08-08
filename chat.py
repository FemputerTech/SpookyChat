"""
This module defines the view for handling GET requests to the home page
of the SpookyChat application.
"""
from flask import render_template
from flask.views import MethodView


class Chat(MethodView):
    """
    Handles the index (home) page.

    Methods:
    -------
    get(): Handles GET requests to the index (home) page.
    post(): Handles the openai chat.
    delete(): Deletes messages from the chat.
    """
    
    def get(self):
        """
        Renders the index (home) page.
        
        Returns:
        --------
        response : str
            The rendered HTML template for the index page.
        """
        return render_template("index.html")


    def post(self):
        return
    

    def delete(self):
        return