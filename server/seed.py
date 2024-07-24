#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker
import random

# Local imports
from app import app
from models import db, Book, Member, Loan
from datetime import datetime, timedelta

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
        # m.password_hash = fake.password(length=8, special_chars=True, digits=True, upper_case=True, lower_case=True)
        m.password_hash = "test1234"
        members.append(m)
    return members

def create_books():
    books = []
    b1 = Book(title='Regulus, vel, Pueri soli sapiunt' , author='Antoine de Saint-Exupéry' , publish_year=2001 , page=83 , image_url='https://covers.openlibrary.org/b/id/115557-L.jpg' , summary="Le Petit Prince est une œuvre de langue française, la plus connue d'Antoine de Saint-Exupéry. Publié en 1943 à New York simultanément à sa traduction anglaise, c'est une œuvre poétique et philosophique sous l'apparence d'un conte pour enfants.\nTraduit en quatre cent cinquante-sept langues et dialectes, Le Petit Prince est le deuxième ouvrage le plus traduit au monde après la Bible.\nLe langage, simple et dépouillé, parce qu'il est destiné à être compris par des enfants, est en réalité pour le narrateur le véhicule privilégié d'une conception symbolique de la vie. Chaque chapitre relate une rencontre du petit prince qui laisse celui-ci perplexe, par rapport aux comportements absurdes des « grandes personnes ». Ces différentes rencontres peuvent être lues comme une allégorie.\nLes aquarelles font partie du texte et participent à cette pureté du langage : dépouillement et profondeur sont les qualités maîtresses de l'œuvre.\nOn peut y lire une invitation de l'auteur à retrouver l'enfant en soi, car « toutes les grandes personnes ont d'abord été des enfants. (Mais peu d'entre elles s'en souviennent.) ». L'ouvrage est dédié à Léon Werth, mais « quand il était petit garçon ».\n\n(Wikipedia)", star=4.41)
    b2 = Book(title='Fear no evil' , author='Anatoly Shcharansky' , publish_year=1988 , page=437 , image_url='https://covers.openlibrary.org/b/id/9156872-L.jpg' , summary='Fear No Evil is a book by the Soviet-Israeli activist and politician Natan Sharansky about his struggle to immigrate to Israel from the former Soviet Union (USSR). The book tells the story of the Jewish refuseniks in the USSR in the 1970s, his show trial on charges of espionage, incarceration by the KGB and liberation' )
    b3 = Book(title='Elon Musk: Tesla, SpaceX, and the Quest for a Fantastic Future' , author='Ashlee Vance' , publish_year=2015 , page=392 , image_url='https://covers.openlibrary.org/b/id/7359078-L.jpg' , summary='In the spirit of Steve Jobs and Moneyball, Elon Musk is both an illuminating and authorized look at the extraordinary life of one of Silicon Valley\'s most exciting, unpredictable, and ambitious entrepreneurs -- a real-life Tony Stark -- and a fascinating exploration of the renewal of American invention and its new "makers." Elon Musk spotlights the technology and vision of Elon Musk, the renowned entrepreneur and innovator behind SpaceX, Tesla, and SolarCity, who sold one of his Internet companies, PayPal, for $1.5 billion. Ashlee Vance captures the full spectacle and arc of the genius\'s life and work, from his tumultuous upbringing in South Africa and flight to the United States to his dramatic technical innovations and entrepreneurial pursuits. Vance uses Musk\'s story to explore one of the pressing questions of our age: can the nation of inventors and creators who led the modern world for a century still compete in an age of fierce global competition? He argues that Musk -- one of the most unusual and striking figures in American business history -- is a contemporary, visionary amalgam of legendary inventors and industrialists including Thomas Edison, Henry Ford, Howard Hughes, and Steve Jobs. More than any other entrepreneur today, Musk has dedicated his energies and his own vast fortune to inventing a future that is as rich and far-reaching as the visionaries of the golden age of science-fiction fantasy. Thorough and insightful, Elon Musk brings to life a technology industry that is rapidly and dramatically changing by examining the life of one of its most powerful and influential titans. - Publisher.' , star=4.15)       
    b4 = Book(title='Control Your Mind and Master Your Feelings' , author='Eric Robertson' , publish_year=2019 , page=231 , image_url='https://covers.openlibrary.org/b/id/12009823-L.jpg' , summary='We oftentimes look towards the outside world to find the roots of our problems. However, most of the times, we should be looking inwards. Our mind and our emotions determine our state of being in the present moment. If those aspects are left unchecked, we can get easily overwhelmed and are left feeling unfulfilled every single day.\n\nThis book contains two manuscripts designed to help you discover the best and most efficient way to control your thoughts and master your feelings.\n\nIn the first part of the bundle called Breaking Overthinking, you will discover:\n\nHow overthinking can be detrimental to your social life.\nThe hidden dangers of overthinking and what can happen to you if it’s left untreated.\nHow to declutter your mind from all the noise of the modern world.\nHow overthinking affects your body, your energy levels, and your everyday mood.\nHow your surroundings affect your state of mind, and what you NEED to do in order to break out of that state.\nBad habits we perform every day and don’t even realize are destroying our sanity (and how to overcome them properly).\nHow to cut out toxic people from your life, which cloud your judgment and make you feel miserable.', star=3.80 )
    b5 = Book(title='Dune' , author='Frank Herbert' , publish_year=1965 , page=541 , image_url='https://covers.openlibrary.org/b/id/7910196-L.jpg' , summary="Set on the desert planet Arrakis, Dune is the story of the boy Paul Atreides, heir to a noble family tasked with ruling an inhospitable world where the only thing of value is the spice melange, a drug capable of extending life and enhancing consciousness. Coveted across the known universe, melange is a prize worth killing for...\n\nWhen House Atreides is betrayed, the destruction of Paul's family will set the boy on a journey toward a destiny greater than he could ever have imagined. And as he evolves into the mysterious man known as Muad'Dib, he will bring to fruition humankind's most ancient and unattainable dream.\n\nA stunning blend of adventure and mysticism, environmentalism and politics, Dune won the first Nebula Award, shared the Hugo Award, and formed the basis of what is undoubtedly the grandest epic in science fiction." , star=4.28)
    b6 = Book(title="Harry Potter and the Philosopher's Stone" , author='J. K. Rowling' , publish_year=1997 , page=352 , image_url='https://covers.openlibrary.org/b/id/12904310-L.jpg' , summary="Harry Potter #1\n\nWhen mysterious letters start arriving on his doorstep, Harry Potter has never heard of Hogwarts School of Witchcraft and Wizardry.\n\nThey are swiftly confiscated by his aunt and uncle.\n\nThen, on Harry’s eleventh birthday, a strange man bursts in with some important news: Harry Potter is a wizard and has been awarded a place to study at Hogwarts.\n\nAnd so the first of the Harry Potter adventures is set to begin." , star=4.25)
    b7 = Book(title='1Q84' , author='Haruki Murakami' , publish_year=2011 , page=925 , image_url='https://covers.openlibrary.org/b/id/11526100-L.jpg' , summary='The novel is a sub-melodramatic sentimental metafictional love story in a ficticious world with two moons in the sky, a thriller packed with cults, assassinations and grotesque sex (newyorkobserver). The title is a play on the Japanese pronunciation of the year 1984 of George Orwell. The novel was longlisted for the 2011 Man Asian Literary Prize and placed No. 2 in Amazon.com\'s top books of the year.' , star=3.81)
    b8 = Book(title='Kitchen' , author="Banana Yoshimoto" , publish_year=1993 , page=152 , image_url='https://covers.openlibrary.org/b/id/6936759-L.jpg' , summary="A scathing comedy of social striving in the suburbs, Absurd Person Singular follows the fortunes of three couples who turn up in each other's kitchens on three successive Christmases, to hilarious and devastating effect." , star=4.23)
    b9 = Book(title='No Longer Human' , author='Osamu Dazai' , publish_year=1948 , page=188 , image_url='https://covers.openlibrary.org/b/id/14550843-L.jpg' , summary="Osamu Dazai's No Longer Human, this leading postwar Japanese writer's second novel, tells the poignant and fascinating story of a young man who is caught between the breakup of the traditions of a northern Japanese aristocratic family and the impact of Western ideas. In consequence, he feels himself \"disqualified from being human\" (a literal translation of the Japanese title). Donald Keene, who translated this and Dazai's first novel, The Setting Sun, has said of the author's work: \"His world . . . suggests Chekhov or possibly postwar France, . . . but there is a Japanese sensibility in the choice and presentation of the material. A Dazai novel is at once immediately intelligible in Western terms and quite unlike any Western book.\" His writing is in some ways reminiscent of Rimbaud, while he himself has often been called a forerunner of Yukio Mishima." , star=4.09)
    b10 = Book(title='Love Poems of Rumi' , author='Rumi' , publish_year=2015 , page=128 , image_url='https://covers.openlibrary.org/b/id/13053139-L.jpg' , summary='Born Jalal ad-Din Mohammad Balkhi in Persia early in the thirteenth century, the poet known as Rumi (named after the city where he lived) composed works of mysticism and desire that inspired countless people in his own time and throughout the centuries. His poems expressed the deepest longings of the human heart for its beloved, for that transcendent intimacy which is the source of the divine.\n\nThis slender, beautiful volume consists of new translations by Farsi scholar Fereydoun Kia, edited by Deepak Chopra to evoke the rich mood and music of Rumi\'s love poems. Exalted yearning, ravishing ecstasy, and consuming desire emerge from these poems as powerfully today as they did on their creation more than 700 years ago.' , star=3.68)
    b11 = Book(title="A Game of Thrones" , author='George R. R. Martin' , publish_year=2011 , page= 806, image_url='https://covers.openlibrary.org/b/id/11293305-L.jpg' , summary="Here is the first volume in George R. R. Martin’s magnificent cycle of novels that includes A Clash of Kings and A Storm of Swords. As a whole, this series comprises a genuine masterpiece of modern fantasy, bringing together the best the genre has to offer. Magic, mystery, intrigue, romance, and adventure fill these pages and transport us to a world unlike any we have ever experienced. Already hailed as a classic, George R. R. Martin’s stunning series is destined to stand as one of the great achievements of imaginative fiction.\n\nA GAME OF THRONESn\n\Long ago, in a time forgotten, a preternatural event threw the seasons out of balance. In a land where summers can last decades and winters a lifetime, trouble is brewing. The cold is returning, and in the frozen wastes to the north of Winterfell, sinister and supernatural forces are massing beyond the kingdom’s protective Wall. At the center of the conflict lie the Starks of Winterfell, a family as harsh and unyielding as the land they were born to. Sweeping from a land of brutal cold to a distant summertime kingdom of epicurean plenty, here is a tale of lords and ladies, soldiers and sorcerers, assassins and bastards, who come together in a time of grim omens.\n\nHere an enigmatic band of warriors bear swords of no human metal; a tribe of fierce wildlings carry men off into madness; a cruel young dragon prince barters his sister to win back his throne; and a determined woman undertakes the most treacherous of journeys. Amid plots and counterplots, tragedy and betrayal, victory and terror, the fate of the Starks, their allies, and their enemies hangs perilously in the balance, as each endeavors to win that deadliest of conflicts: the game of thrones.\n--back cover" , star=4.24)
    books.append(b1)
    books.append(b2)
    books.append(b3)
    books.append(b4)
    books.append(b5)
    books.append(b6)
    books.append(b7)
    books.append(b8)
    books.append(b9)
    books.append(b10)
    books.append(b11)

    return books

# def create_loans():
#     loans = []

#     for _ in range(10):
#         start = "2023-01-01"
#         end = datetime.today() - timedelta(days=30)
#         l = Loan(
#                 loan_date = fake.date_between(start_date=start,end_date=end),
#                 book_id=rc([book.id for book in books]), 
#                 member_id = rc([member.id for member in members])
#         )
#         l.returned_date = l.loan_date + timedelta(days=random.randint(7, 30))
#         loans.append(l)
#     return loans

def create_loans():
    loans = []

    for _ in range(20):
        start = datetime.strptime("2022-01-01", "%Y-%m-%d")
        end = datetime.today() - timedelta(days=40)
        l = Loan(
                loan_date= datetime.strptime(str(fake.date_between_dates(start, end)), "%Y-%m-%d"),
                book_id=rc([book.id for book in books]), 
                member_id = rc([member.id for member in members])
        )
        random_days = random.randint(7, 38)
        l.returned_date = l.loan_date + timedelta(days=random_days)
        loans.append(l)
    return loans


if __name__ == '__main__':
    
    with app.app_context():
        print('Cleaning db...')
        Member.query.delete()
        Book.query.delete()
        Loan.query.delete()

        print("Starting seed...")

        print('Seeding members...')
        members = create_members()
        db.session.add_all(members)
        db.session.commit()

        print('Seeding books...')
        books = create_books()
        db.session.add_all(books)
        db.session.commit()

        print('Seeding loans...')
        loans = create_loans()
        db.session.add_all(loans)
        db.session.commit()

        print("Done seeding!")
