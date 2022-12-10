from flask import Blueprint,render_template,request,flash,redirect,url_for
from flask_login import current_user,login_required
from . import db
from .models import User,Job
rec = Blueprint('rec',__name__)

@rec.route('/home')
@login_required
def home():
    return render_template('rec_home.html',user=current_user)

@login_required
@rec.route('/job',methods=['GET','POST'])
def create_job():
    if request.method=='POST':
        title = request.form.get('title')
        desc = request.form.get('desc')
        job = Job(title=title,desc=desc,user_id=current_user.id)
        db.session.add(job)
        db.session.commit()
        flash('Job Created')
        return redirect(url_for('rec.home'))
    return render_template('job.html',user=current_user)


@rec.route('/update/<id>',methods=['GET','POST'])
@login_required
def update(id):
    if request.method=='POST':
        job = Job.query.filter_by(id=id).first()
        if job:
            title = request.form.get('title')
            desc = request.form.get('desc')
            job.title = title
            job.desc = desc
            db.session.commit()
            flash('Job Updated')
            return redirect(url_for('rec.home'))
        else:
            flash("Job does not exist")
    return render_template('update.html',user=current_user)

@rec.route('/delete/<id>')
@login_required
def delete(id):
    job = Job.query.filter_by(id=id).first()
    if job:
        db.session.delete(job)
        db.session.commit()
        flash('Job Deleted')
        return redirect(url_for('rec.home'))
    else:
        flash("Job does not exist")
    return redirect(url_for('rec.home'))