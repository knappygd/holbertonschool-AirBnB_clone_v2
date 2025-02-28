#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
# from models.base_model import Model
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey



class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    id = Column(String(60), primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

