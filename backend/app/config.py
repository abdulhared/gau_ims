# config.py  (or wherever your Config classes live)
import os

from dotenv import load_dotenv

load_dotenv()  # Load .env right at the top of the config module

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'fallback-dev-key-change-me'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///tickets.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

    EMAIL_ADDRESS = os.environ.get('MAIL_USERNAME')
    EMAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev_tickets.db'


class ProductionConfig(Config):
    # In production you should set DATABASE_URL and MAIL_PASSWORD via real environment variables
    # (Render, Railway, Fly.io, Heroku, Docker secrets, etc.)
    pass