from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:@localhost/flask_crud"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

ma = Marshmallow(app)


book_schema = bookSchema()
books_schema = bookSchema(many=True)



if __name__ == '__main__':
  app.run(debug=True)
