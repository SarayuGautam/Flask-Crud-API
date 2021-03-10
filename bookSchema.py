from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

class book(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), unique=True)
  description = db.Column(db.String(200))
  price = db.Column(db.Float)
  author = db.Column(db.Integer)

  def __init__(self, name, description, price, author):
    self.name = name
    self.description = description
    self.price = price
    self.author = author


class bookSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'description', 'price', 'author')

book_schema = bookSchema()
books_schema = bookSchema(many=True)
