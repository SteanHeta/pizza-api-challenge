from flask import Flask
from server import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object('server.config.Config')
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    with app.app_context():
        from server.controllers.restaurant_controller import restaurants_bp
        from server.controllers.pizza_controller import pizzas_bp
        from server.controllers.restaurant_pizza_controller import restaurant_pizzas_bp
        
        app.register_blueprint(restaurants_bp)
        app.register_blueprint(pizzas_bp)
        app.register_blueprint(restaurant_pizzas_bp)
    
    return app