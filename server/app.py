#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import make_response, request
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
from models import Book, Loan, Member

# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

class Members(Resource):
    def get(self):
        members = Member.query.all()
        members_dict = [member.to_dict() for member in members]
        return make_response(members_dict, 200)

class Books(Resource):
    def get(self):
        books = Book.query.all()
        books_dict = [book.to_dict() for book in books]
        return make_response(books_dict, 200)

class Loans(Resource):
    def get(self):  
        loans = Loan.query.all()
        loans_dict = [loan.to_dict() for loan in loans]
        return make_response(loans_dict, 200)



api.add_resource(Members, '/members')
api.add_resource(Books, '/books')
api.add_resource(Loans, '/loans')

if __name__ == '__main__':
    app.run(port=5555, debug=True)


