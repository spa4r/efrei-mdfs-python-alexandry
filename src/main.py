from flask import Flask, request,jsonify
from flask_restx import Api, Resource,fields
import json

app = Flask(__name__)
api = Api(app=app, version='1.0', title='Books API', description='', validate=True)

ns_books = api.namespace('books', description = "Books operations")
book_definition = api.model('Book Informations', {
    'isbn': fields.Integer(required=True),
    'title': fields.String(required=True),
    'subtitle': fields.String(required=False),
    'author': fields.String(required=True),
    'published': fields.String(required=True),
    'publisher': fields.String(required=True),
    'pages': fields.Integer(required=True),
    'description': fields.String(required=True),
    'website': fields.String(required=False),
})

with open('data/books.json') as json_file:
    data = json.load(json_file)
    books = data["books"]

@ns_books.route("/")
class BooksList(Resource):
    @api.response(200, 'Flask RESTPlus  : Success')
    @api.response(400, 'Flask RESTPlus  : Error')
    def get(self):
        """
        Returns a list of books
        """
        return jsonify(books)

    @api.response(201, 'Flask RESTPlus  : Success')
    @api.response(400, 'Flask RESTPlus  : Error')
    @api.expect(book_definition)
    def post(self):
        """
        Add a new book to the list
        """
        data = request.get_json()
        for i in books:
            if i["isbn"] == data.get('isbn'):
                return {"response": "book already exists."},400
        books.append(data)
        return {"response": "book created"},201

@ns_books.route("/<int:isbn>")
class Book(Resource):

    @api.response(200, 'Flask RESTPlus  : Success')
    @api.response(400, 'Flask RESTPlus  : Error')
    def get(self,isbn):
        """
        Return a selected book
        """
        for i in books:
            if isbn == i["isbn"]:
                return jsonify(i)

    @api.response(201, 'Flask RESTPlus  : Success')
    @api.response(400, 'Flask RESTPlus  : Error')
    @api.expect(book_definition)
    def put(self,isbn):
        """
        Edits a selected book
        """
        data = request.get_json()
        for i in books:
            if i["isbn"] == isbn:
                for key in data.keys():
                    i[key] = data[key]
                    return {"response": "book modified"},201

    @api.response(200, 'Flask RESTPlus  : Success')
    @api.response(400, 'Flask RESTPlus  : Error')
    def delete(self,isbn):
        """
        Delete a selected book
        """
        for i in books:
            if isbn == i["isbn"]:
                books.remove(i)
                return {"response": "book deleted"},200