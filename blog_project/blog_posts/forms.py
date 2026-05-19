from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,TextAreaField
from wtforms.validators import DataRequired

class BlogPostForms(FlaskForm):
    title=StringField("enter title of the blog",validators=[DataRequired()])
    text=TextAreaField("enter yout thoughts here",validators=[DataRequired()])
    submit=SubmitField("post")