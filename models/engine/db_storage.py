#!/usr/bin/python3
"""Engine to save in the data base"""
from sqlalchemy import create_engine
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
from models.state import State
from models.city import City
from models.user import User
from models.review import Review
from models.place import Place
from models.amenity import Amenity
from os import getenv

MySQL_user = getenv("HBNB_MYSQL_USER")
MySQL_password = getenv("HBNB_MYSQL_PWD")
MySQL_host = getenv("HBNB_MYSQL_HOST")
MySQL_database = getenv("HBNB_MYSQL_DB")


class DBStorage:
    """Create class DB"""

    __engine = None
    __session = None

    def __init__(self):
        """Init"""

        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(MySQL_user, MySQL_password,
                                                 MySQL_host, MySQL_database,
                                                 pool_pre_ping=True))

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """All objects"""

        object_dict = {}

        if cls is None:
            objects = self.__session.query(User, State, Review, Place,
                                           City, Amenity).all()

            for obj in objects:
                obj_name = obj.__class__.__name__
                obj_id = obj.id

                key = obj_name + "." + obj_id

                object_dict[key] = obj
        else:
            objects = self.__session.query(cls). all()

            for obj in objects:
                obj_name = obj.__class__.__name__
                obj_id = obj.id

                key = obj_name + "." + obj_id

                object_dict[key] = obj

        return object_dict

    def new(self, obj):
        """Add new obj to db"""
        self.__session.add(obj)

    def save(self):
        """Commit changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an object"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Create all tables in the database
        """
        Base.metadata.create_all(self.__engine)

        Session = scoped_session(sessionmaker(
            bind=self.__engine, expire_on_commit=False
        ))

        self.__session = Session
    
    def close(self):
        """
        call remove() method on the private session attribute
        (self.__session) tips or close() on the class Session
        """
        self.__session.remove()
