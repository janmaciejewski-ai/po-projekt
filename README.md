# Users API

A simple Flask server application for managing users.

## Requirements

- Python 3.8+
- Flask

## Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Navigate to the `users-api` directory.
2. Run the application (make sure to set `PYTHONPATH` if needed, or run as module):
   ```bash
   python -m app.app
   ```
   Or set environment variables:
   ```bash
   export FLASK_APP=app/app.py
   flask run
   ```

## Endpoints

- `GET /users`: List all users.
- `GET /users/<id>`: Get a single user.
- `POST /users`: Create a user. Body: `{"name": "...", "lastname": "..."}`.
- `PATCH /users/<id>`: Update a user partially.
- `PUT /users/<id>`: Create or update a user fully.
- `DELETE /users/<id>`: Delete a user.

## Testing

Run tests with `pytest`:

```bash
pytest
```
