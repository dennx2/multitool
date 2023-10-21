from flask import Flask
from .config import Config

def create_app():

    # App config
    app = Flask(__name__) 
    app.config.from_object(Config)

    # Import Blueprints
    from .routes.main import main_bp
    from .routes.stock import stock_bp
    from .routes.pokemon import pokemon_bp

    # Register Blueprints
    app.register_blueprint(main_bp, url_prefix="/")
    app.register_blueprint(stock_bp, url_prefix="/stock")
    app.register_blueprint(pokemon_bp, url_prefix="/pokemon")

    return app
