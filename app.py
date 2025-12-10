from flask import Flask


def create_app():
    app = Flask(__name__)

    # CONFIGURATION - using ENV

    # PLUGIN INIT - extensions for "app" object

    # REGISTRATION (Blueprints / Routes)
    @app.route("/") # pro testovací účely
    def index():
        return f"""
        Let's deploy my app !
        """
    # APP CONTEXT - where we need to know the structure of the app 

    return app