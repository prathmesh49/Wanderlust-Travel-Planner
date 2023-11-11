from .model import db, Destinations
from flask import render_template, jsonify

class DestinationsDTO:
    @staticmethod
    def get_welcome_message():
        return render_template("index.html")

    @staticmethod
    def get_destinations():
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
        return str(destination_list)
    
    @staticmethod
    def add_destination(data):
        try:

            # Create a new destination instance
            new_destination = Destinations(
                name=data['name'],
                description=data['description'],
                location=data['location']
            )

            # Add the new destination to the database session
            db.session.add(new_destination)
            # Commit the changes to the database
            db.session.commit()

            return jsonify({'message': 'Destination added successfully'}), 201  # 201 Created status code

        except Exception as e:
            return jsonify({'error': str(e)}), 500  # 500 Internal Server Error status code

    @staticmethod
    def patch_destination(destination_id,data):
        try:

            # Find the destination by ID
            destination = Destinations.query.get_or_404(destination_id)

            # Patch (partially update) the destination attributes
            if 'name' in data:
                destination.name = data['name']
            if 'description' in data:
                destination.description = data['description']
            if 'location' in data:
                destination.location = data['location']

            # Commit the changes to the database
            db.session.commit()

            return jsonify({'message': 'Destination patched successfully'}), 200  # 200 OK status code

        except Exception as e:
            return jsonify({'error': str(e)}), 500  # 500 Internal Server Error status code
        
    @staticmethod
    def delete_destination(destination_id):
        try:
            # Find the destination by ID
            destination = Destinations.query.get_or_404(destination_id)

            # Delete the destination from the database
            db.session.delete(destination)
            # Commit the changes to the database
            db.session.commit()

            return jsonify({'message': 'Destination deleted successfully'}), 200  # 200 OK status code

        except Exception as e:
            return jsonify({'error': str(e)}), 500  # 500 Internal Server Error status code