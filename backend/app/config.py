import os
from dotenv import load_dotenv

load_dotenv()  # Load .env variables

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'fallback-dev-key-change-me'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///tickets.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-Mail settings
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'True') == 'True'
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', 'False') == 'True'
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER', os.environ.get('MAIL_USERNAME'))

    
    # ✅ CELERY CONFIG (THIS WAS MISSING)
    CELERY_BROKER_URL = os.environ.get(
        'CELERY_BROKER_URL', 'redis://localhost:6379/0'
    )
    CELERY_RESULT_BACKEND = os.environ.get(
        'CELERY_RESULT_BACKEND', 'redis://localhost:6379/0'
    )
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev_tickets.db'

class ProductionConfig(Config):
    pass
