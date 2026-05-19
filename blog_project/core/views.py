from flask import redirect,render_template,url_for,request,Blueprint
from blog_project.models import Blogpost
core=Blueprint("core",__name__)

@core.route('/')
def index():
    page=request.args.get('page',1,type=int)
    blogposts=Blogpost.query.order_by(Blogpost.date.desc()).paginate(page=page,per_page=5)
    return render_template("index.html",blog_posts=blogposts)

@core.route('/info')
def info():
    return render_template('info.html')