#!/usr/bin/python
"""City-class definition."""
from models.base_model import Base, BaseModel
import models
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """City representation."""
    if models.storage_t == 'db':
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship('Place', cascade='all, delete', backref='city')
    else:
        name = state_id = ''

    def __init__(self, **kwargs):
        """Initialize city."""
        super().__init__(**kwargs)
