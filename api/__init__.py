#!flask/bin/python
from flask import Flask, request, redirect, url_for, session
from flask_session import Session
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
Session(app)

from api import routes

if __name__ == '__main__':
    app.run(debug=True)