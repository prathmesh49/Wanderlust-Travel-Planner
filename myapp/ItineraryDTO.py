from .model import db, Itinerary, Destinations, Expense
from flask import jsonify

class ItineraryDTO:
    
    @staticmethod
    def get_itineraries(destination_id):
        try:
            # Find the destination by ID
            destination = Destinations.query.get_or_404(destination_id)

            # Retrieve itineraries for the specified destination
            itineraries = destination.itineraries

            # Convert itineraries to a list of dictionaries
            itinerary_list = [
                {
                    'id': itinerary.id,
                    'activity': itinerary.activity,
                    'destination_id': itinerary.destination_id,
                }
                for itinerary in itineraries
            ]

            return jsonify({'itineraries': itinerary_list}), 200  # 200 OK status code

        except Exception as e:
            return jsonify({'error': str(e)}), 500  # 500 Internal Server Error status code

    @staticmethod
    def add_itinerary(destination_id, data):
        try:
            # Find the destination by ID
            destination = Destinations.query.get_or_404(destination_id)

            # Create a new itinerary instance
            new_itinerary = Itinerary(
                activity=data['activity'],
                destination_id=destination_id
            )

            # Add the new itinerary to the destination
            destination.itineraries.append(new_itinerary)

            # Add the new itinerary to the database session
            db.session.add(new_itinerary)
            # Commit the changes to the database
            db.session.commit()

            return jsonify({'message': 'Itinerary added successfully'}), 201  # 201 Created status code

        except Exception as e:
            return jsonify({'error': str(e)}), 500  # 500 Internal Server Error status code

    @staticmethod
    def delete_itinerary(itinerary_id):
        try:
            # Find the itinerary by ID
            itinerary = Itinerary.query.get_or_404(itinerary_id)

            # Delete the itinerary from the database
            db.session.delete(itinerary)
            # Commit the changes to the database
            db.session.commit()

            return jsonify({'message': 'Itinerary deleted successfully'}), 200  # 200 OK status code

        except Exception as e:
            return jsonify({'error': str(e)}), 500  # 500 Internal Server Error status code
        
    @staticmethod
    def patch_itinerary(itinerary_id, data):
        try:
            # Find the itinerary by ID
            itinerary = Itinerary.query.get_or_404(itinerary_id)

            # Patch (partially update) the itinerary attributes
            if 'activity' in data:
                itinerary.activity = data['activity']

            # Commit the changes to the database
            db.session.commit()

            return jsonify({'message': 'Itinerary patched successfully'}), 200  # 200 OK status code

        except Exception as e:
            return jsonify({'error': str(e)}), 500  # 500 Internal Server Error status code
