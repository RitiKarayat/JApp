from flask import Blueprint,render_template
from flask_login import current_user

user = Blueprint('user',__name__)

@user.route('/user_home')
def home():
    return render_template('user_home.html',user=current_user)