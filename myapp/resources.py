from flask_restful import Resource, reqparse
from .model import db, Destinations
from .business_logic import BusinessLogic

class DestinationResource(Resource):
    
    def get(self, destination_id):
        destination = Destinations.query.get_or_404(destination_id)
        return {
            'id': destination.id,
            'name': destination.name,
            'description': destination.description,
            'location': destination.location
        }

    def put(self, destination_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help='Name cannot be blank')
        parser.add_argument('description', type=str, required=True, help='Description cannot be blank')
        parser.add_argument('location', type=str, required=True, help='Location cannot be blank')
        args = parser.parse_args()

        destination = Destinations.query.get_or_404(destination_id)
        destination.name = args['name']
        destination.description = args['description']
        destination.location = args['location']

        db.session.commit()
        return {
            'message': 'Destination updated successfully',
            'data': {
                'id': destination.id,
                'name': destination.name,
                'description': destination.description,
                'location': destination.location
            }
        }

    def delete(self, destination_id):
        destination = Destinations.query.get_or_404(destination_id)
        db.session.delete(destination)
        db.session.commit()
        return {
            'message': 'Destination deleted successfully'
        }
    
    def getAll(self):
        result = BusinessLogic.get_destinations()
        return result
