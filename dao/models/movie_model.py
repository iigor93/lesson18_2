from setup_db import db
from marshmallow import Schema, fields
from dao.models.genre_model import Genre
from dao.models.director_model import Director


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    description = db.Column(db.String(200))
    trailer = db.Column(db.String(200))
    rating = db.Column(db.Float)
    year = db.Column(db.Integer)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'))
    genres = db.relationship('Genre')
    directors = db.relationship('Director')


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    rating = fields.Float()
    year = fields.Int()
    genre_id = fields.Int()
    director_id = fields.Int()
