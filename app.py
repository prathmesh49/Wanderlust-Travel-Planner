from flask import Flask, render_template, request
from flask_migrate import Migrate
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

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
