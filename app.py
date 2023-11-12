from flask import Flask, render_template, request
from flask_migrate import Migrate
from myapp.ExpenseDTO import ExpenseDTO
from myapp.ItineraryDTO import ItineraryDTO
from myapp.model import db
from myapp.DestinationsDTO import DestinationsDTO


# Create a Flask application instance
app = Flask(__name__)

# SQLAlchemy Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:4355@localhost/wonderlust'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Initialize SQLAlchemy and Migrate
db.init_app(app)
migrate = Migrate(app, db)

    
# Define a route for the home page
@app.route('/')
def index():
    result = DestinationsDTO.get_welcome_message()
    return result

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

# Destinations Crud Operations

@app.route('/destination')
def getAllDestinations():
    result = DestinationsDTO.get_destinations()
    return result

@app.route('/destination', methods=['POST'])
def add_destination():
    data = request.get_json()    
    result = DestinationsDTO.add_destination(data)
    return result

@app.route('/destination/<int:dest_id>', methods=['PATCH'])
def update_destination(dest_id):
    data = request.get_json()    
    result = DestinationsDTO.patch_destination(dest_id,data)
    return result

@app.route('/destination/<int:dest_id>', methods=['DELETE'])
def delete_destinations(dest_id):
    result = DestinationsDTO.delete_destination(dest_id)
    return result

# Endpoint for Retrieving All Itineraries for a Destination
@app.route('/itinerary/<int:dest_id>')
def get_all_itineraries(dest_id):
    result = ItineraryDTO.get_itineraries(dest_id)
    return result

# Endpoint for Adding an Itinerary to a Destination
@app.route('/itinerary/<int:dest_id>', methods=['POST'])
def add_itinerary(dest_id):
    data = request.get_json()
    result = ItineraryDTO.add_itinerary(dest_id, data)
    return result

# Endpoint for Updating an Itinerary
@app.route('/itinerary/<int:itinerary_id>', methods=['PATCH'])
def update_itinerary(itinerary_id):
    data = request.get_json()
    result = ItineraryDTO.patch_itinerary(itinerary_id, data)
    return result

# Endpoint for Deleting an Itinerary
@app.route('/itinerary/<int:itinerary_id>', methods=['DELETE'])
def delete_itinerary(itinerary_id):
    result = ItineraryDTO.delete_itinerary(itinerary_id)
    return result

# Endpoint for Retrieving All Expenses for an Itinerary
@app.route('/expense/<int:itinerary_id>')
def get_all_expenses(itinerary_id):
    result = ExpenseDTO.get_expenses(itinerary_id)
    return result

# Endpoint for Adding an Expense to an Itinerary
@app.route('/expense/<int:itinerary_id>', methods=['POST'])
def add_expense(itinerary_id):
    data = request.get_json()
    result = ExpenseDTO.add_expense(itinerary_id, data)
    return result

# Endpoint for Updating an Expense
@app.route('/expense/<int:expense_id>', methods=['PATCH'])
def update_expense(expense_id):
    data = request.get_json()
    result = ExpenseDTO.patch_expense(expense_id, data)
    return result

# Endpoint for Deleting an Expense
@app.route('/expense/<int:expense_id>', methods=['DELETE'])
def delete_expense(expense_id):
    result = ExpenseDTO.delete_expense(expense_id)
    return result

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
