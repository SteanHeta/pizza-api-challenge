from flask import Blueprint, jsonify, request
from server.models import RestaurantPizza, Restaurant, Pizza, db

restaurant_pizzas_bp = Blueprint('restaurant_pizzas', __name__)

@restaurant_pizzas_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    
    try:
        price = data['price']
        pizza_id = data['pizza_id']
        restaurant_id = data['restaurant_id']
        
        if not (1 <= price <= 30):
            raise ValueError("Price must be between 1 and 30")
            
        restaurant_pizza = RestaurantPizza(
            price=price,
            pizza_id=pizza_id,
            restaurant_id=restaurant_id
        )
        
        db.session.add(restaurant_pizza)
        db.session.commit()
        
        pizza = Pizza.query.get(pizza_id)
        restaurant = Restaurant.query.get(restaurant_id)
        
        return jsonify({
            'id': restaurant_pizza.id,
            'price': restaurant_pizza.price,
            'pizza_id': restaurant_pizza.pizza_id,
            'restaurant_id': restaurant_pizza.restaurant_id,
            'pizza': {
                'id': pizza.id,
                'name': pizza.name,
                'ingredients': pizza.ingredients
            },
            'restaurant': {
                'id': restaurant.id,
                'name': restaurant.name,
                'address': restaurant.address
            }
        }), 201
        
    except ValueError as e:
        return jsonify({'errors': [str(e)]}), 400
    except KeyError:
        return jsonify({'errors': ['Missing required fields']}), 400
    except Exception:
        return jsonify({'errors': ['Validation error']}), 400