#!/usr/bin/python3
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base



class DBStorage:

    __engine = None
    __session = None

    def __init__(self):
        """Create a new engine instance and session."""

        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST', 'localhost')
        database = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')

        self.__engine = create_engine(f'mysql+mysqldb://{user}:{password}@{host}/{database}',
                                      pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))

        def all(self, cls=None):
        my_dict = {}
        if cls:
            query_result = self.__session.query(cls).all()
            for obj in query_result:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                my_dict[key] = obj
        else:
            classes = [User, State, City, Amenity, Place, Review]
            for cls in classes:
                query_result = self.__session.query(cls).all()
                for obj in query_result:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    my_dict[key] = obj
        return my_dict

        def new(self, obj):
            self.__session.add(obj)

        def save(self):
            self.__session.commit()
        
        def delete(self, obj=None):
            if obj:
                self.__session.delete(obj)

        def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)
