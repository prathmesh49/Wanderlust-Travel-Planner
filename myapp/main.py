from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from app import db




# Create a Flask application instance
app = Flask(__name__)

# SQLAlchemy Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:4355@localhost/wonderlust'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# Create the database and tables
db.create_all()

# # Define Destination model
class Destinations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    location = db.Column(db.String(255), nullable=False)
    # itineraries = db.relationship('Itinerary', backref='destination', lazy=True)
    # Establish one-to-many relationship with Itinerary model
    # itineraries = db.relationship('Itinerary', back_populates='destination', lazy=True)
    itineraries = db.relationship('Itinerary', back_populates='destination', lazy=True, cascade="all, delete-orphan")

# Define Itinerary model
class Itinerary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activity = db.Column(db.String(255), nullable=False)
    # destination_id = db.Column(db.Integer, db.ForeignKey('destination.id'), nullable=False)
    # Establish many-to-one relationship with Destination model
    destination = db.relationship('Destination', back_populates='itineraries')

# Define Expense model
# class Expense(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     description = db.Column(db.String(255), nullable=False)
#     amount = db.Column(db.Float, nullable=False)
#     itinerary_id = db.Column(db.Integer, db.ForeignKey('itinerary.id'), nullable=False)
#     itinerary = db.relationship('Itinerary', backref=db.backref('expenses', lazy=True))

# Define a route for the home page
@app.route('/')
def index():
    return 'Welcome to Wanderlust Travel Planner!'  # Message displayed on the home page

@app.route('/destinations')
def destinations():
    destinations = Destinations.query.all()
    destination_list = []
    for destination in destinations:
        destination_info = {
            'id': destination.id,
            'name': destination.name,
            'description': destination.description,
            'location': destination.location
        }
        destination_list.append(destination_info)
    return str(destination_list)  # Display destinations as a string (for testing purposes)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
