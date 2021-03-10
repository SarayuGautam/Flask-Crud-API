from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:@localhost/flask_crud"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

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
