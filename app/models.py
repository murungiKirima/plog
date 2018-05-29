from app import create_app,db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):

    __tablename__='users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True, index =True)
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    post = db.relationship("Post", backref="user", lazy = "dynamic")
    comment = db.relationship("Comments", backref="user", lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('You can not read the Password Attribute')


    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash, password)


    def __repr__(self):
        return 'User {}'.format(self.username)

class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime)
    blog_post = db.Column(db.Text)

    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comment = db.relationship("Comments", backref="post", lazy = "dynamic")

    def save_post(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_post(cls):
        Post.all_post.clear()

    def get_pitches(id):
        post = Post.query.all()
        return post

class Comments(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db. Integer, primary_key=True)
    comment_id = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(self, id):
        comment = Comments.query.order_by(Comments.date_posted.desc()).filter_by(post_id=id).all()
        return comment