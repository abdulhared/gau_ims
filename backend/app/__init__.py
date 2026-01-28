from flask import Flask
from flask_cors import CORS

from app.extensions import db, migrate, mail

def create_app(config_name='development'):
    app = Flask(__name__)

    # Load config
    app.config.from_object(f'app.config.{config_name.capitalize()}Config')
    

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)  # Initialize mail with app
    CORS(app)

    # Register routes
    from app.routes.ticket import ticket_bp
    from app.utils.email_service import email_bp
    
    app.register_blueprint(ticket_bp, url_prefix='/api')
    app.register_blueprint(email_bp, url_prefix='/api')
    

    return app
