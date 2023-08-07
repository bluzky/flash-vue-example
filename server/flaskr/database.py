from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

db = SQLAlchemy()

class Base():
    """Base model defined shared columns"""
    id =  db.Column(db.Integer, primary_key=True)
    inserted_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

Base = declarative_base(cls=Base)
