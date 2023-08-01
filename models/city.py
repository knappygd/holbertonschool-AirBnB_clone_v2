#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
# from models.base_model import Model
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    state_id = ""
    name = ""
    places = relationship("Place", backref="cities", cascade="delete")
