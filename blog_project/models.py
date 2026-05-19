from blog_project import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):
    
    __tablename__ = 'users'

    id=db.Column(db.Integer,primary_key=True)
    profile_image=db.Column(db.String(64),nullable=False,default='default_profile.png')
    username=db.Column(db.String(64),index=True)
    email=db.Column(db.String(64),unique=True,index=True)
    password_hash=db.Column(db.String(128))

    posts = db.relationship('Blogpost', backref='author', lazy=True)
    
    def __init__(self,email,username,password):
        self.email=email
        self.username=username
        self.password_hash=generate_password_hash(password)

    def validate_password(self,password):
        return check_password_hash(self.password_hash,password)
    
    def __repr__(self):
        return f"username:{self.username}"

class Blogpost(db.Model):
    __tablename__ = 'blogpost'
    users = db.relationship(User)
    
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    date=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    title=db.Column(db.String(64),nullable=True)
    text=db.Column(db.Text,nullable=False)
    
    def __init__(self,user_id,title,text):
        self.user_id=user_id
        self.title=title
        self.text=text
    
    def __repr__(self):
        return f"post_id: {self.user_id}"
    pass
