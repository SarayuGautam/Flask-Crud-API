from flask import Flask

import os
from bookSchema import db, ma

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:@localhost/flask_crud"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

ma.init_app(app)

from bookBlueprint import book_bp

app.register_blueprint(book_bp, url_prefix="")

if __name__ == '__main__':
  app.run(debug=True)
