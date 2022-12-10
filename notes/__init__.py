import os 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()
db_name='db'
def create_app():
    app = Flask(__name__,instance_relative_config=True)
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_name}'
    db.init_app(app)
    from .models import User
    with app.app_context():
        if not os.path.exists(f'instance/{db_name}'):
            db.create_all()
            print("DB")
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
   
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    #from .blueprints import auth
    #auth = Blueprint('auth',__name__)
    from .auth import auth
    app.register_blueprint(auth)
    from .rec import rec
    app.register_blueprint(rec)
    from .user import user
    app.register_blueprint(user)

    



    return app

