from flask import Flask
from flask_migrate import Migrate
from myapp.model import db
from myapp.business_logic import BusinessLogic
from flask_restful import Api
from myapp.resources import DestinationResource


# Create a Flask application instance
app = Flask(__name__)

# SQLAlchemy Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:4355@localhost/wonderlust'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Initialize SQLAlchemy and Migrate
db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)

    
# Define a route for the home page
@app.route('/')
def index():
    result = BusinessLogic.get_welcome_message()
    return result

api.add_resource(DestinationResource, '/destination/<int:destination_id>')

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
