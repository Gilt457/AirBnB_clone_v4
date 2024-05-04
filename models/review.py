#!/usr/bin/python3
"""Defines the Review class."""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """Class for creating Review objects."""
    if models.storage_t == 'db':
        __tablename__ = 'reviews'  # Sets the table name for database storage.
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""  # Placeholder for place ID when not using a database.
        user_id = ""  # Placeholder for user ID when not using a database.
        text = ""  # Placeholder for review text when not using a database.

    def __init__(self, *args, **kwargs):
        """Initializes a new Review instance."""
        super().__init__(*args, **kwargs)
