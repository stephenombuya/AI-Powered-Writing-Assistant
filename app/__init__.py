from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app(config=None):
    """Application factory function"""
    app = Flask(__name__)
    
    # Configure the app
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///writing_assistant.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
    
    # Override config if provided
    if config:
        app.config.update(config)
    
    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Register blueprints
    from app.routes import bp as main_bp
    app.register_blueprint(main_bp)
    
    # Create upload directory if it doesn't exist
    os.makedirs(os.path.join(app.instance_path, 'exports'), exist_ok=True)
    
    # Register error handlers
    @app.errorhandler(404)
    def not_found_error(error):
        return {'error': 'Resource not found'}, 404
    
    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return {'error': 'Internal server error'}, 500
    
    # CLI commands
    @app.cli.command("init-db")
    def init_db():
        """Initialize the database."""
        db.create_all()
        print('Database initialized.')
    
    @app.cli.command("clean-exports")
    def clean_exports():
        """Clean up old export files."""
        export_dir = os.path.join(app.instance_path, 'exports')
        for file in os.listdir(export_dir):
            if os.path.getmtime(os.path.join(export_dir, file)) < time.time() - 86400:  # 24 hours
                os.remove(os.path.join(export_dir, file))
        print('Export directory cleaned.')
    
    # Health check endpoint
    @app.route('/health')
    def health_check():
        return {'status': 'healthy'}, 200
    
    return app

# Factory pattern usage
def init_app():
    """Initialize the core application."""
    app = create_app()
    
    # Ensure all tables exist
    with app.app_context():
        db.create_all()
    
    return app
