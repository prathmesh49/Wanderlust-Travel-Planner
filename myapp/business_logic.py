from .model import Destinations
from flask import render_template

class BusinessLogic:
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
