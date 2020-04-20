from flask import Flask, session,request,render_template,flash,logging,redirect,url_for
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dt
import csv

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://yvbnsamypdykrt:66a8025afaeff05c9e7831afa8e680df238ecd3e14a79fae3863764e7cd4e6cc@ec2-54-197-48-79.compute-1.amazonaws.com:5432/daqbm9qlg9jo7o'

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)



class Books(db.Model):
    __tablename__="books"
    isbn=db.Column(db.String,primary_key=True)
    title=db.Column(db.String,nullable=False)
    author=db.Column(db.String,nullable=False)
    year=db.Column(db.String,nullable=False)

    def __init__(self,isbn,title,author,year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year

def main():
    db.create_all()
    f = open("books.csv")
    reader = csv.reader(f)
    for isbn,title,author,year in reader:
        book = Books(isbn=isbn, title=title, author=author,year=year)
        db.session.add(book)
        print(f"Added book of year {year} ,isbn: {isbn},title: {title} ,author: {author}.")
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        main()