from flask import Blueprint,render_template,redirect,url_for,flash
from flask_login import current_user,login_required
from .models import Job,User
from . import db
user = Blueprint('user',__name__)

@user.route('/user_home')
@login_required
def home():
    jobs = Job.query.all()
    return render_template('user_home.html',user=current_user,jobs=jobs)

@user.route('/fav/<uid>/<jid>/<op>',methods=['POST'])
def fav(uid,jid,op):
    if op=='add':
        user = User.query.filter_by(id=uid).first()
        print(user.jobs_fav_id)
        if user:
            job = Job.query.filter_by(id=jid).first()
            if job:
                if user.jobs_fav_id==None:
                    user.jobs_fav_id = str(jid)+' '
                    db.session.commit()
                elif jid in user.jobs_fav_id:
                    flash('Already Added')
                else:
                    user.jobs_fav_id += str(jid)+' '
                    db.session.commit()
                print(user.jobs_fav_id)
        return 'Added'
    else:
        user = User.query.filter_by(id=uid).first()
        print(user.jobs_fav_id)
        if user:
            job = Job.query.filter_by(id=jid).first()
            if job:
                # if user.jobs_fav_id==None:
                #     return redirect(url_for('user.home'),user=current_user)
                #     #db.session.commit()
                # else:
                jids = user.jobs_fav_id.split(' ')
                jids.remove(jid)
                user.jobs_fav_id = ' '.join(jids)
                
                db.session.commit()
                print(user.jobs_fav_id)
                return redirect(url_for('user.allfav',uid=uid))
        return 'Removed'

@user.route('/allfav/<uid>',methods=['GET'])
def allfav(uid):
    user = User.query.filter_by(id=uid).first()
    #print(user.jobs_fav_id)
    if user:
        #jids = user.jobs_fav_id
        #print(jids)
        jobs = Job.query.all()
        return render_template('fav.html',user=current_user,jobs=jobs)
