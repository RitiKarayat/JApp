from flask import Blueprint,render_template
from flask_login import current_user
rec = Blueprint('rec',__name__)

@rec.route('/home')
def home():
    return render_template('rec_home.html',user=current_user)