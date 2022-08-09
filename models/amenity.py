#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.place import place_amenity
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """An amenity"""
 
    __tablename__ = 'amenities'
    
    name = Column(String(128), nullable=False)
    
    place_amenities = relationship("Place", backref="place_amenity", secondary=place_amenity)
    
    # name = ""
