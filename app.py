from flask import Flask
from flask_migrate import Migrate
from myapp.model import db
from myapp.business_logic import BusinessLogic


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
    result = BusinessLogic.get_welcome_message()
    return result

@app.route('/destinations')
def destinations():
   result = BusinessLogic.get_destinations()
   return result

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
