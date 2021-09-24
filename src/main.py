from flask import Flask, request
from flask_restx import Api, Resource
import json

app = Flask(__name__)
api = Api(app=app, version='1.0', title='Books API', description='', validate=True)

ns_books = api.namespace('books', description = "Books operations")
    
@ns_books.route("/")
class BooksList(Resource):
    @api.response(200, 'Flask RESTPlus  : Success')
    @api.response(400, 'Flask RESTPlus  : Error')
    def get(self):
        """
        Returns a list of books
        """
        file = open('./data/books.json', 'r')
        data = []
        for book in file:
            data.append(book)

        return {"response": data}

    @api.response(200, 'Flask RESTPlus  : Success')
    @api.response(400, 'Flask RESTPlus  : Error')
    def post(self):
        """
        Add a new book to the list
        """

@ns_books.route("/<int:id>")
class Book(Resource):

    @api.response(200, 'Flask RESTPlus  : Success')
    @api.response(400, 'Flask RESTPlus  : Error')
    def get(self,id):
        """
        Return a selected book
        """

    @api.response(200, 'Flask RESTPlus  : Success')
    @api.response(400, 'Flask RESTPlus  : Error')
    def put(self,id):
        """
        Edits a selected book
        """

    @api.response(200, 'Flask RESTPlus  : Success')
    @api.response(400, 'Flask RESTPlus  : Error')
    def delete(self,id):
        """
        Delete a selected book
        """