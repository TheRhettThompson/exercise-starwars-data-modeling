import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    username = Column(String(250) , nullable=False)
    password = Column(String(250) , nullable=False)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer , primary_key=True)
    character_name = Column(String(250))
    planet_from = Column(String(250) , ForeignKey('planets.name'))
    age = Column(Integer)


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    size = Column(Integer)
    population = Column(Integer)
    climate = Column(String(250))
   
    
class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer , primary_key=True)
    name = Column(String(250))
    vehicle_type = Column(String(250))
    pilot = (String(250) , ForeignKey('character.name'))


class Favorites(Base):
    __tablename__ = 'favorites'
    user_id = Column(Integer)
    date_added = Column(Integer)
    favorite_characters = Column(String(250) , ForeignKey('character.name'))
    favorite_planets = Column(String(250))
    favorite_vehicles = Column(String(250))



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
