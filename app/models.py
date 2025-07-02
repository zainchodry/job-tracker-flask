from app.extensions import db
from datetime import datetime
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), unique = True, nullable = True)
    email = db.Column(db.String(100), nullable = False, unique = False)
    password = db.Column(db.String(100), nullable = False)
    jobs = db.relationship('Job', backref = "user", lazy = True)




class Job(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    company = db.Column(db.String(100), nullable = False)
    role = db.Column(db.String(100), nullable = False)
    link = db.Column(db.String(100))
    status = db.Column(db.String(100), default = 'Applied')
    deadline = db.Column(db.Date)
    notes = db.Column(db.Text)
    date_applied = db.Column(db.DateTime, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)


    def __repr__(self) -> str:
        return f"{self.company} - {self.role}"
    




