import sys

"""
With sqlalchemy, we can write a single Python file to set up
and configure our database:
"""

"""
Init 1st Part Configuration
"""
from sqlalchemy import  Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

"""
In order to create our Foreign Key relationships
"""
from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()
"""
End 1st Part Configuration
"""

class Restaurant(Base):
	__tablename__ = "restaurant"
	name = Column(String(80), nullable = False)
	id = Column(Integer, primary_key = True)
class MenuItem(Base):
	__tablename__ = "menu_item"
	name = Column(String(80), nullable = False)
	id = Column(Integer, primary_key = True)
	course = Column(String(250))
	description = Column(String(250))
	price = Column(String(8))
	restaurant_id = Column(Integer,ForeignKey("restaurant.id"))
	restaurant = relationship(Restaurant)

"""
Init 1st Part Configuration
"""
engine = create_engine(
'sqlite:///restaurantmenu.db')

Base.metadata.create_all(engine)
"""
End 1st Part Configuration
"""