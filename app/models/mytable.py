# app/repository/models.py
from app.repository.db import db
from sqlalchemy import Column, Integer, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base # import the module to define a base class for models
Base = declarative_base() # define a base class for models

class MYTABLE(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    country = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"<User {self.name}>"
    
class DATALOGGER(Base):
    __tablename__ = 'DATALOGGER' # specify the table name

    ID = Column(Integer, primary_key=True) # specify the id column as primary key
    DATE = Column(DateTime) # specify the DATE column as string type with length 50
    TEMP = Column(Float) # specify the TEMP column as string type with length 50

    def __repr__(self): # define a representation method for printing objects
        return f"<DATALOGGER(ID={self.ID}, DATE={self.DATE}, TEMP={self.TEMP})>"