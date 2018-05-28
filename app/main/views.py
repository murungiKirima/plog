from flask import Flask, render_template, request, redirect, url_for
from . import main
from ..models import Post
from datetime import datetime

@main.route('/')
def index():
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('index.html', posts=posts)

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.filter_by(id=post_id).one()

    return render_template('post.html', post=post)

@main.route('/add')
def add():
    return render_template('add.html')

@main.route('/addPost',methods=['POST'])
def addPost():
    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    post = request.form['post']

    post = Post(title=title, subtitle=subtitle, author=author, blog_post=post, date_posted=datetime.now())

    db.session.add(post)
    db.session.commit()

    return redirect(url_for('index'))