## Pizza API Challenge
A simple RESTful Flask API for managing restaurants, pizzas, and their pricing. Built using Flask, SQLAlchemy, and Flask-Migrate.

## Project Structure
server/ ├── app.py # App factory ├── config.py # DB config ├── models/ │ ├── init.py │ ├── pizza.py │ ├── restaurant.py │ └── restaurant_pizza.py ├── controllers/ │ ├── init.py │ ├── pizza_controller.py │ └── restaurant_controller.py ├── seed.py # DB seed script migrations/ # Alembic migrations README.md # You're here

## Setup Instructions
Clone the repository:
```
git clone https://github.com/DenzelMwangi001/pizza-api-challenge.git cd pizza-api-challenge 
```
## Set up your virtual environment:
```
python3 -m venv venv 
source venv/bin/activate
``` 
# On Windows use venv\Scripts\activate 
```
pip install -r requirements.txt
```
## Set environment variables:
bash 
```export FLASK_APP=server.app:create_app 
export FLASK_ENV=development
```
 Run migrations and seed the database:

bash
``` 
flask db init 
```# Run once 
```flask db migrate -m "Initial migration" 
flask db upgrade 
python -m server.seed``` Run the server:

bash 
```
flask run
```
## API Endpoints Get all restaurants bash Copy Edit GET /restaurants Get a single restaurant by ID

bash 
```
GET /restaurants/int:id Delete a restaurant
```
bash 
```
DELETE /restaurants/int:id Get all pizzas
```
bash 
```
GET /pizzas Create a new restaurant pizza (assign pizza to restaurant)
```
bash 
```
POST /restaurant_pizzas Content-Type: application/json
```

{ "price": 12, "pizza_id": 1, "restaurant_id": 2 } 🧪 Testing (via Postman) Use the provided Postman collection to test the API endpoints.

## Tech Stack Python 3

Flask

SQLAlchemy

Flask-Migrate

SQLite (Dev)

Author Denzel Mwangi GitHub

## About
No description, website, or topics provided.
Resources
 Readme
 Activity
Stars
 0 stars
Watchers
 0 watching
Forks
 0 forks
Report repository
Releases
No releases published
Packages
No packages published
Languages
Python
100.0%
Footer
