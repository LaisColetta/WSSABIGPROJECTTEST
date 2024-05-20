# Recipe Management Web Application

This is a Flask web application for managing recipes. It allows users to view, add, update, and delete recipes through both a web interface and a RESTful API.

## Features

- View a list of all recipes.
- Add a new recipe.
- Update an existing recipe.
- Delete a recipe.
- Search for recipes online using the Spoonacular API and add them to the database.

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/recipe-management.git
    ```

2. Navigate to the project directory:

    ```bash
    cd recipe-management
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the configuration file (`config.py`) and add your Spoonacular API key:

    ```python
    SPOONACULAR_API_KEY = 'your-spoonacular-api-key'
    ```

## Usage

1. Run the Flask application locally:

    ```bash
    python app.py
    ```

2. Access the application in your web browser at `http://localhost:5000`.

3. Use the web interface to manage recipes or make requests to the RESTful API endpoints for programmatic access.

## Accessing the Online Server

This application is also hosted on [PythonAnywhere](https://www.pythonanywhere.com/). You can access the online server by following these steps:

1. Visit the [PythonAnywhere](https://www.pythonanywhere.com/) website and sign up for an account if you don't have one already.

2. Once logged in, navigate to the Dashboard and open a Bash console.

3. Clone the repository into your PythonAnywhere account:

    ```bash
    git clone https://github.com/your-username/recipe-management.git
    ```

4. Navigate to the project directory:

    ```bash
    cd recipe-management
    ```

5. Set up the configuration file (`config.py`) and add your Spoonacular API key:

    ```python
    SPOONACULAR_API_KEY = 'your-spoonacular-api-key'
    ```

6. Run the Flask application:

    ```bash
    python app.py
    ```

7. Access the application in your web browser using the PythonAnywhere domain provided.

## API Endpoints

- `GET /api/recipes`: Get all recipes.
- `GET /api/recipes/{recipe_id}`: Get a specific recipe by ID.
- `POST /api/recipes`: Create a new recipe.
- `PUT /api/recipes/{recipe_id}`: Update an existing recipe.
- `DELETE /api/recipes/{recipe_id}`: Delete a recipe.
- `POST /api/recipes/search`: Search for recipes online and add them to the database.


