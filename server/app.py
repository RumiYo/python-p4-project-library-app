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

    def post(self):
        json_data = request.get_json()
        new_record = Member(
            first_name=json_data.get('first_name'),
            last_name=json_data.get('last_name'),
            user_id=json_data.get('user_id'),
            email=json_data.get('email'),
        )
        db.session.add(new_record)
        db.session.commit()
        if not new_record.id:
            return {'error': ['validation errors']}, 400
        return make_response(new_record.to_dict(), 201)

class MemberById(Resource):
    def get(self,id):
        member = Member.query.filter(Menber.id==id).first()
        if not member: 
            return {'error': 'Member not found'}, 404
        return make_response(member.to_dict(), 200)

    def patch(self,id):
        member = Member.query.filter(Menber.id==id).first()
        if not member: 
            return {'error': 'Member not found'}, 404
        json_data = request.get_json()
        if "@" not in json_data.get('email'):
            return {'error': ['validation errors']}, 400
        if 'email' in json_data:
            member.email = json_data.get('email')
        
        db.session.add(member)
        db.session.commit()

    def delete(self,id):
        member = Member.query.filter(Menber.id==id).first()
        if not member: 
            return {'error': 'Member not found'}, 404
        db.session.delete(member)

class Books(Resource):
    def get(self):
        books = Book.query.all()
        books_dict = [book.to_dict() for book in books]
        return make_response(books_dict, 200)

class BookById(Resource):
    class get(self, id):
        book = Book.query.filter(Bool.id==id).first()
        if not book:
            return {'error': 'Book not found'}, 404
        return make_response(book.to_dict(), 202)

class Loans(Resource):
    def get(self):  
        loans = Loan.query.all()
        loans_dict = [loan.to_dict() for loan in loans]
        return make_response(loans_dict, 200)



api.add_resource(Members, '/members')
api.add_resource(MemberByID, '/members/<int:id>')
api.add_resource(Books, '/books')
api.add_resource(BookById, '/books/<init:id>')
api.add_resource(Loans, '/loans')

if __name__ == '__main__':
    app.run(port=5555, debug=True)


