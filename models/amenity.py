#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
# from models.base_model import Base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    __tablename__ = "amenities"
    id = Column(String(60), primary_key=True)
    name = Column(String(128), nullable=False)
    place_amenities = relationship(
        "Place",
        secondary="place_amenity",
        viewonly=False
    )
