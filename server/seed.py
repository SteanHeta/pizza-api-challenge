from server import create_app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    pizza1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")
    pizza2 = Pizza(name="Pepperoni", ingredients="Tomato, Mozzarella, Pepperoni")

    rest1 = Restaurant(name="Pizza Palace", address="123 Main St")
    rest2 = Restaurant(name="Slice Heaven", address="456 Broadway")

    db.session.add_all([pizza1, pizza2, rest1, rest2])
    db.session.commit()

    rp1 = RestaurantPizza(price=12, pizza_id=pizza1.id, restaurant_id=rest1.id)
    rp2 = RestaurantPizza(price=20, pizza_id=pizza2.id, restaurant_id=rest2.id)

    db.session.add_all([rp1, rp2])
    db.session.commit()
