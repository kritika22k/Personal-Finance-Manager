# config.py

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # You can change this to your DB URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
