#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.review import Review
# from models.base_model import Base
from models import storage
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Amenity(BaseModel):
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship(
        "Place",
        secondary="place_amenity",
        viewonly=False
    )
