from server import db
from server.models import Restaurant, Pizza, RestaurantPizza

def seed_database():

    db.drop_all()
    db.create_all()

    restaurants = [
        Restaurant(name="Pizza Palace", address="123 Main St"),
        Restaurant(name="Mario's Pizzeria", address="456 Oak Ave"),
        Restaurant(name="Luigi's Pizza", address="789 Pine Rd")
    ]
    db.session.add_all(restaurants)

    pizzas = [
        Pizza(name="Margherita", ingredients="Tomato sauce, mozzarella, basil"),
        Pizza(name="Pepperoni", ingredients="Tomato sauce, mozzarella, pepperoni"),
        Pizza(name="Vegetarian", ingredients="Tomato sauce, mozzarella, bell peppers, mushrooms, onions")
    ]
    db.session.add_all(pizzas)

    db.session.commit()

    restaurant_pizzas = [
        RestaurantPizza(price=10, pizza_id=1, restaurant_id=1),
        RestaurantPizza(price=12, pizza_id=2, restaurant_id=1),
        RestaurantPizza(price=15, pizza_id=3, restaurant_id=2),
        RestaurantPizza(price=8, pizza_id=1, restaurant_id=3),
        RestaurantPizza(price=9, pizza_id=2, restaurant_id=3)
    ]
    db.session.add_all(restaurant_pizzas)

    db.session.commit()

if __name__ == '__main__':
    from server.app import create_app
    app = create_app()
    with app.app_context():
        seed_database()
    print("Database seeded successfully!")