# app/repository/models.py
from app.repository.db import db

class MYTABLE(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    country = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"<User {self.name}>"