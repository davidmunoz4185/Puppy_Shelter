import sys

"""
With sqlalchemy, we can write a single Python file to set up
and configure our database:
"""

"""
Init 1st Part Configuration
"""
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Numeric

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

class Shelter(Base):
	__tablename__ = "shelter"
	id = Column(Integer, primary_key = True)
	name = Column(String(80), nullable = False)
	address = Column(String(250))
	city = Column(String(250))
	state = Column(String(250))
	zipCode = Column(String(10))
	website = Column(String(50))
	
class Puppy(Base):
	__tablename__ = "puppy"
	id = Column(Integer, primary_key = True)
	dateOfBirth = Column(Date)
	name = Column(String(80), nullable = False)
	gender = Column(String(10), nullable = False)
	weight = Column(Numeric(10))
	picture = Column(String)
	shelter_id = Column(Integer,ForeignKey("shelter.id"))
	shelter = relationship(Shelter)
	

"""
Init 1st Part Configuration
"""
engine = create_engine(
'sqlite:///puppyShelter.db')

Base.metadata.create_all(engine)
"""
End 1st Part Configuration
"""
