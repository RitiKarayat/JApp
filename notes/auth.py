#from . import auth
from flask import Blueprint, render_template, redirect, url_for, request,flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user,logout_user,current_user,login_required
from .models import User
from . import db

auth = Blueprint('auth',__name__)

@auth.route('/')
@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        email = request.form.get('email')
        
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password,password):
            return redirect(url_for('auth.login'))
        login_user(user,remember=True)
        flash('Logged in','success')
        print(user.is_recruiter,type(user.is_recruiter))
        if user.is_recruiter:
            
            return redirect(url_for('rec.home'))
        else:
            return redirect(url_for('user.home'))

    return render_template('login.html',user=current_user)


@auth.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        role = request.form.get('role')
        user = User.query.filter_by(email=email).first()
        if not user:
            if password1==password2:
                hashed_pass = generate_password_hash(password1)
                is_recruiter = False
                if role=='Recruiter':
                    is_recruiter = True
                
                new_user = User(email=email,username=username,password=hashed_pass,is_recruiter=is_recruiter)
                db.session.add(new_user)
                db.session.commit()
                #login_user(user,remember=True)
                if is_recruiter:
                    login_user(new_user,remember=True)
                    return redirect(url_for('rec.home'))
                login_user(new_user,remember=True)
                return redirect(url_for('user.home'))
            else:
                flash('Passwords do not match')
        return redirect(url_for('auth.register'))
        

    return render_template('register.html',user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))