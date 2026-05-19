from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired,EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField,FileAllowed

from flask_login import current_user
from blog_project.models import User

class LoginForm(FlaskForm):
    email=StringField("Email",validators=[DataRequired()])
    Password=PasswordField("Password",validators=[DataRequired()])
    Submit=SubmitField("LOGIN")

class RegisterForm(FlaskForm):
    username=StringField("enter name",validators=[DataRequired()])
    email=StringField("enter E-mail",validators=[DataRequired()])
    Password=PasswordField("password",validators=[DataRequired(),EqualTo('c_password')])
    c_password=PasswordField("confirm password",validators=[DataRequired()])
    submit=SubmitField("register!")
    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError ("email has been regester already!")
        
class Update_form(FlaskForm):
    email=StringField("email",validators=[DataRequired()])
    username=StringField("name",validators=[DataRequired()])
    picture=FileField("update profile pic",validators=[FileAllowed(['jpg','png'])])
    submit=SubmitField("update!")
        