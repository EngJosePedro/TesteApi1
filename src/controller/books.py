from flask import Flask
from flask_restplus import Api, Resource

from src.server.instance import server

app, api = server.app, server.api

books_db = [
    {'id': 0, 'title': "Book 1"},
    {'id': 1, 'title': "Book 2"}
    ]

@api.route("/books")
class BookList(Resource):
    """description of class"""

    def get(self, ):
        return books_db
    def post(self, ):
        response = api.payload
        books_db.append(response)
        return response, 200

@api.route("/1")
class testInit(Resource):
    """description of class"""
    def _hello_world(self,):
        return "Hello World beachhh"

    def get(self, ):
        return self._hello_world()
    def post(self, ):
        response = api.payload
        books_db.append(response)
        return response, 200

