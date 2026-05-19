import os
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app=Flask(__name__)
app.config['SECRET_KEY']='mykey'

#__________________db_setup______________
basedir=os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db=SQLAlchemy(app)
Migrate(app,db)

#____________loginconfig______________

login_manager=LoginManager()
login_manager.init_app(app)
login_manager.login_view='users.login'


#___________________blue print___________________
from blog_project.core.views import core
from blog_project.error_pages.handlers import error_pages
from blog_project.user.views import users
from blog_project.blog_posts.views import blog_posts
app.register_blueprint(core)
app.register_blueprint(error_pages)
app.register_blueprint(users)
app.register_blueprint(blog_posts)