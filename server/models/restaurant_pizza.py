from server import db
from sqlalchemy import CheckConstraint

class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)

    __table_args__ = (
        CheckConstraint('price >= 1 AND price <= 30', name='check_price_range'),
    )

    def __repr__(self):
        return f'<RestaurantPizza ${self.price}>'