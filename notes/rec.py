from flask import Blueprint,render_template,request,flash,redirect,url_for
from flask_login import current_user,login_required
from . import db
import os 
from . import UPLOAD_FOLDER
from werkzeug.utils import secure_filename
from .models import User,Job
rec = Blueprint('rec',__name__)

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


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
        if 'image' not in request.files:
            flash('No file part')
            return redirect(url_for('rec.home'))
        file = request.files['image']
        filename = store_file(file)
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        
        
        job = Job(title=title,desc=desc,img_path=filename,user_id=current_user.id)
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
            os.remove(os.path.join(UPLOAD_FOLDER,job.img_path))
            title = request.form.get('title')
            desc = request.form.get('desc')
            file = request.files['image']
            filename = store_file(file)
            job.title = title
            job.desc = desc
            job.img_path = filename
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
        os.remove(os.path.join(UPLOAD_FOLDER,job.img_path))
        db.session.delete(job)
        db.session.commit()
        #os.remove(os.join)
        flash('Job Deleted')
        return redirect(url_for('rec.home'))
    else:
        flash("Job does not exist")
    return redirect(url_for('rec.home'))



def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def store_file(file):
    if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER,filename)
        #print(url_for('static'))
        file.save(filepath)
        print(filepath,filename)
        return filename