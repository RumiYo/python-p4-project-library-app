from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin

from config import db, bcrypt

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
    star = db.Column(db.Float)

    # Add relationships
    loans = db.relationship('Loan', back_populates='book')
    members = association_proxy('loans', 'member',
                    creator=lambda project_obj: Loan(project=project_obj))

    @validates('star')
    def validate_star(self, key, star):
        if star < 0.00 or star > 5.00:
            raise ValueError('Star must be between 0 and 5')
        return star

    def __repr__(self):
        return f'<Book {self.id}: {self.title}, {self.author}, {self.publish_year}, {self.page}, {self.image_url}, {self.summary}>'


class Member(db.Model, SerializerMixin):
    __tablename__='members'
    serialize_rules = ('-loans.member','-books.members', '-books.loans')

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    user_id = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False)
    _password_hash = db.Column(db.String, nullable=False)

    # Add relationships
    loans = db.relationship('Loan', back_populates='member')
    books = association_proxy('loans', 'book',
                creator=lambda project_obj: Loan(project=project_obj))

    #email validation
    @validates('email')
    def validate_email(self, key, email):
        if '@' not in email:
             raise ValueError("Email address validation error")
        return email

    #passsword handling
    @hybrid_property
    def password_hash(self):
        raise AttributeError('Password hash is not accessible')

    @password_hash.setter
    def password_hash(self, password):
        if password is None:
            raise ValueError("Password cannot be None")
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8')
        )
        self._password_hash = password_hash.decode('utf-8')
    
    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8')
        )

    # def to_dict(self):
    #     return{
    #         "id": self.id,
    #         "first_name": self.first_name, 
    #         "last_name": self.last_name,
    #         "user_id": self.user_id,
    #         "email": self.email,

    #     }

    def __repr__(self):
        return f'<Member {self.id}: {self.first_name}, {self.last_name}, {self.user_id}, {self.email}>'

class Loan(db.Model, SerializerMixin):
    __tablename__ = 'loans'
    serialize_rules = ('-book.loans', '-member.books','member.loans')

    id = db.Column(db.Integer, primary_key=True)
    loan_date = db.Column(db.Date, server_default=db.func.now())
    returned_date = db.Column(db.Date)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    member_id = db.Column(db.Integer, db.ForeignKey('members.id'))
    # Add relationships
    book = db.relationship('Book', back_populates='loans')
    member = db.relationship('Member', back_populates='loans')
    __table_args__ = ( 
        db.CheckConstraint('loan_date < returned_date', name='check_loan_date_before_returned_date' ),
        )

    def __repr__(self):
        return f'<Loan {self.id}: {self.loan_date}, {self.returned_date}. {self.book_id}, {self.member_id}>'
