#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker
import random

# Local imports
from app import app
from models import db, Book, Member, Loan

fake = Faker()

def create_members():
    members = []
    for _ in range(10):
        m = Member(
            first_name = fake.first_name(),
            last_name = fake.last_name(),
            email = fake.email()         
        )
        m.user_id = f"{m.first_name}{random.randint(10,100)}"
        members.append(m)
    return members

if __name__ == '__main__':
    
    with app.app_context():
        print('Cleaning db...')
        Member.query.delete()

        print("Starting seed...")
        # Seed code goes here!

        print('Seeding members...')
        members = create_members()
        db.session.add_all(members)
        db.session.commit()

        print("Done seeding!")
