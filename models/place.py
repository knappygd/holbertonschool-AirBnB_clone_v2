#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.review import Review
from models.amenity import Amenity
# from models.base_model import Base
from models import storage
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Table
from sqlalchemy.orm import relationship

place_amenity = Table(
    "place_amenity",
    Base.metadata,
    Column(
        "place_id",
        String(60),
        ForeignKey("places.id"),
        primary_key=True,
        nullable=False
    ),
    Column(
        "amenity_id",
        String(60),
        ForeignKey("amenities.id"),
        primary_key=True,
        nullable=False
    ),
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), nullable=False)
    user_id = Column(String(60), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    reviews = relationship("Review", backref="place", cascade="delete")

    @property
    def review(self):
        """Returns the list of Review instances."""
        reviews = []
        for rev in list(storage.all(Review).values()):
            if rev.place_id == self.id:
                reviews.append(rev)
        return reviews

    @property
    def amenities(self):
        amenities = []
        for amenity in list(storage.all(Amenity).values()):
            if amenity.id == self.amenity_ids:
                amenities.append(amenity)
        return amenities

    @amenities.setter
    def amenities(self, value):
        if type(value) == Amenity:
            self.amenity_ids.append(value.id)
