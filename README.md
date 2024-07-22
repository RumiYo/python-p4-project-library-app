# Online Library App 
Flatiron Softwear engineer course phase 4 project 

## Table of Contents
* [Phase 4 project requirement](#phase-4-project-requirements)
* [My Full-Stack application](#my-full-stack-application)
* [Technologies](#technologies)
* [Resources](#resources)


## Phase 4 project requirements

[Project guidelines are here. ](https://github.com/learn-co-curriculum/python-p4-phase-4-project)

For this project, you must:

1. Use a Flask API backend with a React frontend.
2. Have at least three models on the backend, that include the following:
  a. At least two one-to-many relationships.
  b.At least one reciprocal many-to-many relationship.
  c. The many-to-many association model/table must have a user submittable attribute, i.e. an attribute aside from the foreign keys.
  d. Full CRUD actions for at least one resource.
  e. Minimum of create and read actions for EACH resource.
3. Use forms and validation through Formik on all input.
  a. At least one data type validation.
  b. At least one string/number format validation.
4. Have at least three different client-side routes using React Router. Be sure to include a nav bar or other UI element that allows users to navigate between routes.
5. Connect the client and server using fetch().

## My Full-Stack application
This online library application allowed users to browse books and to loan/return books after the login. The whole loaned histories and user information change is available on Account Summary page too.

#### Backend:
- Python and Flask for building the API
- SQLAlchemy for database management
- Serialization and validation

#### Frontend:
- React for building the user interface
- Sending HTTP requests with fetch to the API
- React Router for navigation
- Formik and Form Validation

## Technologies

### Password Protection
Instead of storing users' passwords in plain text, we store a hashed version of them for the security purpose.
```
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

```

### Authentication in Flask
Authentication is to provide one's identity to an application in order to access protected information; logging in.
UserID and password combination is the most popular authentication mechanism, and it is also known as password authentication.
```
class Signups(Resource):

    def post(self):
        json_data = request.get_json()
        if not json_data.get('user_id') or not json_data.get('first_name') or not json_data.get('last_name')or not json_data.get('email'):
            return {"error": "All input fields cannot be empty"}, 422 
        duplicate_name_member = Member.query.filter(Member.user_id==json_data['user_id']).first()
        if duplicate_name_member:
            return {"error": "This user_id already exists. Try with a new user id"}, 422
        new_record = Member(
            first_name=json_data.get('first_name'),
            last_name=json_data.get('last_name'),
            user_id=json_data.get('user_id'),
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
```

### Formik Form Validation
The Formik library provides us a hook to give initial values to the form and write a onSubmit callback function to do something with the values that were submitted. 
```
import React, { useState } from "react";
import { useFormik } from 'formik';
import * as yup from "yup";

function SignUpForm({ onSignUp }){

    const [error, setError] = useState("");
    const [isLoading, setIsLoading] = useState(false);


  const formSchema = yup.object().shape({
    first_name: yup.string().required("Must enter First Name").max(15),
    last_name: yup.string().required("Must enter Last Name").max(15),
    user_id: yup.string().required("Must enter a UserID").max(10),
    email: yup.string().email("Invalid email").required("Must enter email"),
    password_hash: yup.string().required("Must enter First Name").max(15),
  });

    const formik = useFormik({
      initialValues: {
        first_name: "",
        last_name: "",
        user_id: "",
        email: "",
        password_hash: "",
      },
      validationSchema: formSchema,
      onSubmit: (values) => {
        setIsLoading(true);
        fetch("/signup", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(values),
        })
        .then((r) => {
          setIsLoading(false);
          if (r.ok) {
            r.json().then((member) => onSignUp(member));
          } else {
            r.json().then((err) => setError(err.error));
          }
        })
      }
    })

    return (
        <div>
            <h2>Signup Form</h2>
            <form className="LoginSignupForms" onSubmit={formik.handleSubmit}>
              <p>Please fill out all the information below:</p>
                <label htmlFor="first_name">First Name:  </label>
                <input
                type="text"
                id="first_name"
                autoComplete="off"
                value={formik.values.first_name}
                onChange={formik.handleChange}
                />

                {/* ....other input forms are here...... */}
                
                <input type="submit" className="buttons"/>

                <p>{error}</p>
            </form>            
        </div>
    )
}

export default SignUpForm;
```

## Resources

- [DBDiagram](https://dbdiagram.io/d)
- [Open Library Search API](https://openlibrary.org/dev/docs/api/search)
- [WorldCat](https://search.worldcat.org/lists/136b83c4-1076-4655-868e-66bafb8e99c3)
- [Faker 26.0.0 documentation: date_time](https://faker.readthedocs.io/en/master/providers/faker.providers.date_time.html)
- [Python Formik Validation](https://github.com/learn-co-curriculum/python-formik-validation)
- [python-p4-iam-putting-it-all-together-lab](https://github.com/RumiYo/python-p4-iam-putting-it-all-together-lab/tree/main/client/src/components)
- [Coolors](https://coolors.co/palette/cb997e-eddcd2-fff1e6-f0efeb-ddbea9-a5a58d-b7b7a4)

