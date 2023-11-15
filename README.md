
# Wanderlust Travel Planner API Documentation

## Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Wanderlust-Travel-Planner.git
cd Wanderlust-Travel-Planner
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Database

- Choose a database system (e.g., MySQL, PostgreSQL, SQLite).
- Update the database connection settings in the configuration file (`config.py`).

### 5. Run the Application

```bash
python app.py
```

The application will run at `http://127.0.0.1:5000/`.

## API Endpoints

### Destinations

#### 1. Get All Destinations

- **URL:** `/destination`
- **Method:** `GET`
- **Response:**
  ```json
  [
    {
      "id": 1,
      "name": "Destination Name",
      "description": "Destination Description",
      "location": "Destination Location"
    },
    // ... other destinations
  ]
  ```

#### 2. Add a Destination

- **URL:** `/destination`
- **Method:** `POST`
- **Request:**
  ```json
  {
    "name": "New Destination",
    "description": "New Destination Description",
    "location": "New Destination Location"
  }
  ```
- **Response:**
  ```json
  {
    "message": "Destination added successfully"
  }
  ```

#### 3. Update a Destination

- **URL:** `/destination/<int:dest_id>`
- **Method:** `PATCH`
- **Request:**
  ```json
  {
    "name": "Updated Destination Name"
  }
  ```
- **Response:**
  ```json
  {
    "message": "Destination patched successfully"
  }
  ```

#### 4. Delete a Destination

- **URL:** `/destination/<int:dest_id>`
- **Method:** `DELETE`
- **Response:**
  ```json
  {
    "message": "Destination deleted successfully"
  }
  ```


### Itineraries

#### 1. Get All Itineraries for a Destination

- **URL:** `/itinerary/<int:dest_id>`
- **Method:** `GET`
- **Response:**
  ```json
  [
    {
      "id": 1,
      "activity": "Itinerary Activity 1"
    },
    {
      "id": 2,
      "activity": "Itinerary Activity 2"
    },
    // ... other activities
  ]
  ```

#### 2. Add an Itinerary to a Destination

- **URL:** `/itinerary/<int:dest_id>`
- **Method:** `POST`
- **Request:**
  ```json
  {
    "activity": "New Itinerary Activity"
  }
  ```
- **Response:**
  ```json
  {
    "message": "Itinerary added successfully"
  }
  ```

#### 3. Update an Itinerary

- **URL:** `/itinerary/<int:itinerary_id>`
- **Method:** `PATCH`
- **Request:**
  ```json
  {
    "activity": "Updated Itinerary Activity"
  }
  ```
- **Response:**
  ```json
  {
    "message": "Itinerary patched successfully"
  }
  ```

#### 4. Delete an Itinerary

- **URL:** `/itinerary/<int:itinerary_id>`
- **Method:** `DELETE`
- **Response:**
  ```json
  {
    "message": "Itinerary deleted successfully"
  }
  ```

### Expenses

#### 1. Get All Expenses for an Itinerary

- **URL:** `/expense/<int:itinerary_id>`
- **Method:** `GET`
- **Response:**
  ```json
  [
    {
      "id": 1,
      "description": "Expense Description 1",
      "amount": 50.0,
      "itinerary_id": 1
    },
    {
      "id": 2,
      "description": "Expense Description 2",
      "amount": 30.0,
      "itinerary_id": 1
    },
    // ... other expenses
  ]
  ```

#### 2. Add an Expense to an Itinerary

- **URL:** `/expense/<int:itinerary_id>`
- **Method:** `POST`
- **Request:**
  ```json
  {
    "description": "New Expense Description",
    "amount": 25.0
  }
  ```
- **Response:**
  ```json
  {
    "message": "Expense added successfully"
  }
  ```

#### 3. Update an Expense

- **URL:** `/expense/<int:expense_id>`
- **Method:** `PATCH`
- **Request:**
  ```json
  {
    "amount": 40.0
  }
  ```
- **Response:**
  ```json
  {
    "message": "Expense patched successfully"
  }
  ```

#### 4. Delete an Expense

- **URL:** `/expense/<int:expense_id>`
- **Method:** `DELETE`
- **Response:**
  ```json
  {
    "message": "Expense deleted successfully"
  }
  ```


