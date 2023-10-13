from flask import Flask
from .config import Config

def create_app():

    # App config
    app = Flask(__name__) 
    app.config.from_object(Config)

    # Import Blueprints
    from .routes.views import views
    from .routes.stock import stock
    from .routes.pokemon import pokemon

    # Register Blueprints
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(stock, url_prefix="/stock")
    app.register_blueprint(pokemon, url_prefix="/pokemon")

    return app
