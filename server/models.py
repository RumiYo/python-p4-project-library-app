from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Models go here!
class Book(db.Model, SerializerMixin):
    __tablename__ = 'books'
    serialize_rules = ('-loans.book', '-members.books','-members.loans')

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    publish_year = db.Column(db.Integer)
    page = db.Column(db.Integer)
    image_url = db.Column(db.String)
    summary = db.Column(db.String)

    # Add relationships
    loans = db.relationship('Loan', back_populates='book')
    members = association_proxy('loans', 'member',
                    creator=lambda project_obj: Loan(project=project_obj))

    def __repr__(self):
        return f'<Book {self.id}: {self.title}, {self.author}, {self.publish_year}, {self.page}, {self.image_url}, {self.summary}>'


class Member(db.Model, SerializerMixin):
    __tablename__='members'
    serialize_rules = ('-loans.member','-books.members', '-books.loans')

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    user_id = db.Column(db.String, nullable=False, unique=True)
    # password = 
    email = db.Column(db.String, nullable=False)

    # Add relationships
    loans = db.relationship('Loan', back_populates='member')
    books = association_proxy('loans', 'book',
                creator=lambda project_obj: Loan(project=project_obj))

    def __repr__(self):
        return f'<Member {self.id}: {self.first_name}, {self.last_name}, {self.user_id}, {self.email}>'

class Loan(db.Model, SerializerMixin):
    __tablename__ = 'loans'
    serialize_rules = ('-book.loans', '-member.books','member.loans')

    id = db.Column(db.Integer, primary_key=True)
    loan_date = db.Column(db.DateTime, server_default=db.func.now())
    returned_date = db.Column(db.DateTime)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    member_id = db.Column(db.Integer, db.ForeignKey('members.id'))
    # Add relationships
    book = db.relationship('Book', back_populates='loans')
    member = db.relationship('Member', back_populates='loans')

    def __repr__(self):
        return f'<Loan {self.id}: {self.loan_date}, {self.returned_date}. {self.book_id}, {self.member_id}>'
