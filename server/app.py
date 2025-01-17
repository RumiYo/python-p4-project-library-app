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
        if not json_data.get('username') or not json_data.get('first_name') or not json_data.get('last_name')or not json_data.get('email'):
            return {"error": "All input fields cannot be empty"}, 422 
        duplicate_name_member = Member.query.filter(Member.username==json_data['username']).first()
        if duplicate_name_member:
            return {"error": "This username already exists. Try with a new user id"}, 422
        new_record = Member(
            first_name=json_data.get('first_name'),
            last_name=json_data.get('last_name'),
            username=json_data.get('username'),
            email=json_data.get('email'),
        )
        new_record.password_hash = json_data.get('password_hash')
        db.session.add(new_record)
        db.session.commit()
        print(new_record.to_dict())

        if not new_record.id:
            return {'error': 'validation errors'}, 400
        session['user_id'] = new_record.id
        return make_response(new_record.to_dict(), 201)

class CheckSession(Resource):
    def get(self):
        member = Member.query.filter(Member.id==session.get('user_id')).first()
        if member:
            return member.to_dict()
        else:
            return {'error': '401: Not Authorized'}, 401     

class Login(Resource):
    def post(self):
        json_data = request.get_json()
        member = Member.query.filter(Member.username==json_data.get('username')).first()
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
            username=json_data.get('username'),
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

        if 'email' in json_data and "@" not in json_data.get('email'):
            return {'error': 'validation errors'}, 400

        for key, value in json_data.items():
            if hasattr(member, key):
                setattr(member, key, value)
            else:
                return {'error': f'Invalid field: {key}'}, 400
        
        db.session.commit()
        return make_response(member.to_dict(), 200)

    def delete(self,id):
        member = Member.query.filter(Member.id==id).first()
        if not member: 
            return {'error': 'Member not found'}, 404
        db.session.delete(member)
        db.session.commit()

class Books(Resource):
    def get(self):
        books = Book.query.all()
        books_dict = [book.to_dict() for book in books]
        return make_response(books_dict, 200)

    def post(self):
        json_data = request.get_json()
        new_record = Book(
            title = json_data.get('title'),
            author = json_data.get('author'),
            publish_year = json_data.get('publish_year'),
            page = json_data.get('page'),
            image_url = json_data.get('image_url'),
            summary = json_data.get('summary'),
            star = json_data.get('star')
        )
        db.session.add(new_record)
        db.session.commit()
        return make_response(new_record.to_dict(), 201)

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
            return { "error": "validation errors" }, 400
        loan.returned_date = returned_date
        db.session.add(loan)
        db.session.commit()

        return make_response(loan.to_dict(), 202)

    def delete(self, id):
        loan = Loan.query.filter(Loan.id==id).first()
        if not loan: 
            return {'error': 'Loan not found'}, 404
        db.session.delete(loan)
        db.session.commit()

# Live coding 
# /book_loans/3
# Return all of the books with at least that number of loans
# get 

class Bookloaned(Resource):
    def get(self, number):
        books = Book.query.all()
        for book in books: 
            if len(book.loans) >= number:
                booksloaned.append(book)
        if not booksloaned:
            return {'error': 'No data'}
        books_dict = [book.to_dict() for book in booksloaned]
        return make_response(books_dict, 200)




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
api.add_resource(Bookloaned, '/book_loaned/<int:number>')


if __name__ == '__main__':
    app.run(port=5555, debug=True)


