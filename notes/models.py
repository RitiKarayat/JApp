from . import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "user"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    is_recruiter = db.Column(db.Boolean,default=False,nullable=False)
    jobs = db.relationship('Job',backref='user',lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username

class Job(db.Model):
    __tablename__ = "job"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    desc = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))