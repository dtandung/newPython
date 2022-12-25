from app import db
from flask_login import UserMixin
from app import login

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))
    posts = db.relationship("Post", backref="author", lazy=True)

    def __repr__(self):
        return f"Username is: {self.username}"

    def check_password(self, password):
        return self.password == password
    def set_password(self, password):
        self.password = password

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(128))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Post content is: {self.content}"

class LoaiMon(db.Model):
    maloai = db.Column(db.String(64), primary_key= True)
    tenloai = db.Column(db.String(64))

    