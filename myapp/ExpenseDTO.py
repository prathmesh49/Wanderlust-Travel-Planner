from .model import db, Itinerary, Destinations, Expense
from flask import jsonify

class ExpenseDTO:
    @staticmethod
    def get_expenses(itinerary_id):
        try:
            # Find the itinerary by ID
            itinerary = Itinerary.query.get_or_404(itinerary_id)

            # Retrieve expenses for the specified itinerary
            expenses = itinerary.expenses

            # Convert expenses to a list of dictionaries
            expense_list = [
                {
                    'id': expense.id,
                    'description': expense.description,
                    'amount': expense.amount,
                    'itinerary_id': expense.itinerary_id,
                }
                for expense in expenses
            ]

            return jsonify({'expenses': expense_list}), 200  # 200 OK status code

        except Exception as e:
            return jsonify({'error': str(e)}), 500  # 500 Internal Server Error status code

    @staticmethod
    def add_expense(itinerary_id, data):
        try:
            # Find the itinerary by ID
            itinerary = Itinerary.query.get_or_404(itinerary_id)

            # Create a new expense instance
            new_expense = Expense(
                description=data['description'],
                amount=data['amount'],
                itinerary_id=itinerary_id
            )

            # Add the new expense to the itinerary
            itinerary.expenses.append(new_expense)

            # Add the new expense to the database session
            db.session.add(new_expense)
            # Commit the changes to the database
            db.session.commit()

            return jsonify({'message': 'Expense added successfully'}), 201  # 201 Created status code

        except Exception as e:
            return jsonify({'error': str(e)}), 500  # 500 Internal Server Error status code

    @staticmethod
    def patch_expense(expense_id, data):
        try:
            # Find the expense by ID
            expense = Expense.query.get_or_404(expense_id)

            # Patch (partially update) the expense attributes
            if 'description' in data:
                expense.description = data['description']
            if 'amount' in data:
                expense.amount = data['amount']

            # Commit the changes to the database
            db.session.commit()

            return jsonify({'message': 'Expense patched successfully'}), 200  # 200 OK status code

        except Exception as e:
            return jsonify({'error': str(e)}), 500  # 500 Internal Server Error status code

    @staticmethod
    def delete_expense(expense_id):
        try:
            # Find the expense by ID
            expense = Expense.query.get_or_404(expense_id)

            # Delete the expense from the database
            db.session.delete(expense)
            # Commit the changes to the database
            db.session.commit()

            return jsonify({'message': 'Expense deleted successfully'}), 200  # 200 OK status code

        except Exception as e:
            return jsonify({'error': str(e)}), 500  # 500 Internal Server Error status code
