#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    id = Column(String(60), primary_key=True)
    name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    import models

    if models.storage_type != "db":
        @property
        def cities(self):
            from models import storage
            city_objs = storage.all(City)
            return [city for city in city_objs.values()
                    if city.state_id == self.id]
