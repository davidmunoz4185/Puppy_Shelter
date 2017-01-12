
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
engine = create_engine("sqlite:///restaurantmenu.db")

Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)

session = DBSession()

myFirstRestaurant = Restaurant(name = "Pizza Palace")
cheesePizza = MenuItem(name = "Cheese Pizza", description = "Made with all natural ingredients", course = "Entree", price = "$8.99", restaurant = myFirstRestaurant)

urbanVeggieBurger = session.query(MenuItem).filter_by(id = 13).one()
print urbanVeggieBurger.price

urbanVeggieBurger.price = "$2.99"
session.add(urbanVeggieBurger)
session.commit()

veggieBurgers = session.query(MenuItem).filter_by(name = "Veggie Burger")
for veggieBurger in veggieBurgers:
	if veggieBurger.price != "$2.99":
		veggieBurger.price = "$2.99"
		session.add(veggieBurger)
		session.commit()
	print veggieBurger.id
	print veggieBurger.price
	print veggieBurger.restaurant.name
	print "\n"

