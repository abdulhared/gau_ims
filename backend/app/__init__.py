from flask import Flask
from .extensions import db, migrate, mail
from app.celery_app import init_celery
from flask_cors import CORS

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
    from app.routes.ticket_actions import ticket_actions_bp
    
    
    app.register_blueprint(ticket_bp, url_prefix='/api')
    app.register_blueprint(ticket_actions_bp, url_prefix='/api')


    # ✅ Initialize Celery
    app.celery_app = init_celery(app)

    # ✅ IMPORT TASKS (THIS REGISTERS THEM)
    import app.tasks.task 
    

    return app
