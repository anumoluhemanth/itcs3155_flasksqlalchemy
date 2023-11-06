# TODO - Create SQLAlchemy DB and Movie model
from flask_sqlalchemy import SQLAlchemy
#from app import app
db=SQLAlchemy()
# db=SQLAlchemy(app)

class MovieModel(db.Model):
    __tablename__ = "movie"

    movie_id = db.Column(db.Integer, autoincrement=True, nullable = False, primary_key=True)
    title = db.Column(db.String(255), nullable = False)
    director = db.Column(db.String(255),  nullable = False, primary_key=True)
    rating = db.Column(db.Integer)