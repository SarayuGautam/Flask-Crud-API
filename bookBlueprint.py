
from flask import Blueprint, request, jsonify

from bookSchema import db, book, book_schema, books_schema


book_bp = Blueprint("book_bp",__name__)

@book_bp.route('/book', methods=['POST'])
def add_book():
  name = request.json['name']
  description = request.json['description']
  price = request.json['price']
  author = request.json['author']

  new_book = book(name, description, price, author)

  db.session.add(new_book)
  db.session.commit()

  return book_schema.jsonify(new_book)


@book_bp.route('/book', methods=['GET'])
def get_books():
  all_books = book.query.all()
  result = books_schema.dump(all_books)
  return jsonify(result)


@book_bp.route('/book/<id>', methods=['GET'])
def get_book(id):
  book = book.query.get(id)
  return book_schema.jsonify(book)


@book_bp.route('/book/<id>', methods=['PUT'])
def update_book(id):
  book = book.query.get(id)

  name = request.json['name']
  description = request.json['description']
  price = request.json['price']
  author = request.json['author']

  book.name = name
  book.description = description
  book.price = price
  book.author = author

  db.session.commit()

  return book_schema.jsonify(book)

@book_bp.route('/book/<id>', methods=['DELETE'])
def delete_book(id):
  book = book.query.get(id)
  db.session.delete(book)
  db.session.commit()

  return book_schema.jsonify(book)
