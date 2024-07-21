#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import make_response, request, session
from flask_restful import Resource
from datetime import datetime

# Local imports
from config import app, db, api
# Add your model imports
from models import Book, Loan, Member

# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

class Signups(Resource):

    def post(self):
        json_data = request.get_json()
        if not json_data.get('user_id') or not json_data.get('first_name') or not json_data.get('last_name')or not json_data.get('email'):
            return {"message": "All input fields cannot be empty"}, 422 
        duplicate_name_member = Member.query.filter(Member.user_id==json_data['user_id']).first()
        if duplicate_name_member:
            return {"message": "This user_id already exists. Try with a new user id"}, 422
        new_record = Member(
            first_name=json_data.get('first_name'),
            last_name=json_data.get('last_name'),
            user_id=json_data.get('user_id'),
            email=json_data.get('email'),
        )
        new_record.password_hash = json_data.get('password')
        db.session.add(new_record)
        db.session.commit()

        session['user_id'] = new_record.id
        return make_response(new_record.to_dict(), 201)

class CheckSession(Resource):
    def get(self):
        member = Member.query.filter(Member.id==session.get('user_id')).first()
        if member:
            return member.to_dict()
        else:
            return {'mesage': '401: Not Authorized'}, 401     

class Login(Resource):
    def post(self):
        json_data = request.get_json()
        member = Member.query.filter(Member.user_id==json_data.get('user_id')).first()
        if member and member.authenticate(json_data.get('password')):
            session['user_id'] = member.id
            return member.to_dict()

        return {'error': 'Invalid username or password'}, 401

class Logout(Resource):
    def delete(self):
        if not session['user_id']:
            return {'error': 'You are not logged in'}, 401

        session['user_id']= None
        return {}, 204

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
        member = Member.query.filter(Member.id==id).first()
        if not member: 
            return {'error': 'Member not found'}, 404
        return make_response(member.to_dict(), 200)

    def patch(self,id):
        member = Member.query.filter(Member.id==id).first()
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
        member = Member.query.filter(Member.id==id).first()
        if not member: 
            return {'error': 'Member not found'}, 404
        db.session.delete(member)

class Books(Resource):
    def get(self):
        books = Book.query.all()
        books_dict = [book.to_dict() for book in books]
        return make_response(books_dict, 200)

class BookById(Resource):
    def get(self, id):
        book = Book.query.filter(Book.id==id).first()
        if not book:
            return {'error': 'Book not found'}, 404
        return make_response(book.to_dict(), 202)

class Loans(Resource):
    def get(self):  
        loans = Loan.query.all()
        loans_dict = [loan.to_dict() for loan in loans]
        return make_response(loans_dict, 200)

    def post(self):
        json_data = request.get_json()
        new_record = Loan(
            loan_date = datetime.now().date(),
            book_id = json_data.get('book_id'),
            member_id = json_data.get('member_id'),
        )
        db.session.add(new_record)
        db.session.commit()
        return make_response(new_record.to_dict(), 201)

class LoanById(Resource):
    def get(self, id):
        loan = Loan.query.filter(Loan.id==id).first()
        if not loan:
            return {'error': 'Loan not found'}, 404
        return make_response(loan.to_dict(), 200)
    
    def patch(self, id):
        loan = Loan.query.filter(Loan.id==id).first()
        if not loan:
            return {'error': 'Loan not found'}, 404  
        returned_date = datetime.now().date()
        if loan.loan_date > returned_date:
            return { "errors": ["validation errors"] }, 400
        loan.returned_date = returned_date
        db.session.add(loan)
        db.session.commit()

        return make_response(loan.to_dict(), 202)

api.add_resource(Signups, '/signup')
api.add_resource(CheckSession, '/check_session')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(Members, '/members')
api.add_resource(MemberById, '/members/<int:id>')
api.add_resource(Books, '/books')
api.add_resource(BookById, '/books/<int:id>')
api.add_resource(Loans, '/loans')
api.add_resource(LoanById, '/loans/<int:id>')


if __name__ == '__main__':
    app.run(port=5555, debug=True)


