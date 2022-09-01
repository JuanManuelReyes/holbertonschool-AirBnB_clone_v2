#!/usr/bin/python3
""" State Module for HBNB project """
from webbrowser import get
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


# class State(BaseModel, Base):
#     """ The state class, contains relationship and name """

#     __tablename__ = "states"

#     name = Column(String(128), nullable=False)

#     cities = relationship("City", backref="state")

#     if getenv("HBNB_TYPE_STORAGE") != "db":
#         @property
#         def cities(self):
#             """Returns the list of cities"""
#             all_cities = self.cities
#             cities_array = []
#             for key, value in all_cities.items():
#                 if self.id == value.state_id:
#                     cities_array.append(value)

#             return cities_array

class State(BaseModel, Base):
    """ State class """
    type_storage = os.getenv("HBNB_TYPE_STORAGE")
    __tablename__ = "states"

    if type_storage == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        name = ""

    @property
    def cities(self):
        """devolver una lista de instancias de city"""
        inst_list = []
        list_objects = models.storage.all(City)
        for city in list_objects.values():
            if city.state_id == self.id:
                inst_list.append(city)
        return inst_list