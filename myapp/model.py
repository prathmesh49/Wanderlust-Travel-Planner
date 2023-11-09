from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define Destination model
class Destinations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    location = db.Column(db.String(255), nullable=False)
    
    # Define one-to-many relationship with Itinerary
    itineraries = db.relationship('Itinerary', backref='destinations', lazy=True)

    def __repr__(self):
        return f'<Destination {self.name}>'
    
    
    
class Itinerary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activity = db.Column(db.String(255), nullable=False)

    destination_id = db.Column(db.Integer, db.ForeignKey('destinations.id'), nullable=False)

    def __repr__(self):
        return f'<Itinerary {self.activity}>'


class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.Float, nullable=False)

    # Define many-to-many relationship with Itinerary using an association table
    itinerary_id = db.Column(db.Integer, db.ForeignKey('itinerary.id'), nullable=False)
    itinerary = db.relationship('Itinerary', backref=db.backref('expenses', lazy=True))

    def __repr__(self):
        return f'<Expense {self.description}>'
