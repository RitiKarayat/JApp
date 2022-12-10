from flask import Blueprint,render_template
from flask_login import current_user,login_required
from .models import Job
user = Blueprint('user',__name__)

@user.route('/user_home')
@login_required
def home():
    jobs = Job.query.all()
    return render_template('user_home.html',user=current_user,jobs=jobs)