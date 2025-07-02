import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret-key'
    SQLALCHEMY_DATABASE_URI = "sqlite:///job.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = True