from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin): #inherit from db.model class provided by flask and also inherit from Usermixin class
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(100), unique=True)
    password=db.Column(db.String(150))
    first_Name=db.Column(db.String(150))
    notes=db.relationship('Note')  #Capital since its a relationship
    
    #user model is setup

class Note(db.Model):    #this class are like the tables in database
    id=db.Column(db.Integer, primary_key=True)
    data=db.Column(db.String(10000))
    date=db.Column(db.DateTime(timezone=True), default=func.now()) #for automatically adding date (func does this)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id')) #User class is represented as user in sql (ForeignKey thats how sql alchemy works)



    
    


    
    
    