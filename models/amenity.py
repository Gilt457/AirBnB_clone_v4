#!/usr/bin/python3
""" Amenity class definition """
from models import storage_t
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ Amenity entity representation """
    __tablename__ = 'amenities' if storage_t == 'db' else ''
    name = Column(String(128), nullable=False) if storage_t == 'db' else ''

    def __init__(self, **kwargs):
        """ Initializes Amenity instance """
        super(Amenity, self).__init__(**kwargs)
