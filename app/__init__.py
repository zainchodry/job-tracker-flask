from flask import Flask
from app.extensions import db, migrate, logi_manager
import os
from config import Config
from app.models import User
from flask_login import current_user

def create_app():
    app = Flask(__name__, template_folder=os.path.abspath('templates'))
    app.config.from_object(Config)

    db.init_app(app)
    logi_manager.init_app(app)
    migrate.init_app(app, db)

    @logi_manager.user_loader
    def user_loader(user_id):
        return User.query.get(int(user_id))
    
    @app.context_processor
    def inject_user():
        return dict(current_user = current_user)
    
    
    logi_manager.login_view = "main.login"



    from app.routes import main
    app.register_blueprint(main)


    with app.app_context():
        db.create_all()

    

    return app