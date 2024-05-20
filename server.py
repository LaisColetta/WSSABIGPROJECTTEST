from flask import Flask, render_template, jsonify, abort, request
from recipesDAO import recipesDAO
from config import config as cfg
import logging

app = Flask(__name__, template_folder='templates')
app.config.from_object(cfg)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/api/config', methods=['GET'])
def get_config():
    return jsonify({
        'API_URL': "https://api.edamam.com/search",
        'API_ID': app.config['API_ID'],
        'API_KEY': app.config['API_KEY']
    })

# Routes for web interface
@app.route('/')
def index():
    logging.info("Accessing index page...")
    return render_template('index.html')

# Routes for REST API
@app.route('/api/recipes', methods=['GET'])
def get_recipes():
    logging.info("Accessing GET /api/recipes...")
    recipes = recipesDAO.get_all()
    return jsonify(recipes)

@app.route('/api/recipes', methods=['POST'])
def create_recipe():
    logging.info("Accessing POST /api/recipes...")
    data = request.json
    logging.info(f"Received data: {data}")
    if not data or 'name' not in data or 'ingredients' not in data or 'instructions' not in data:
        logging.error("Invalid data received.")
        return jsonify({'error': 'Invalid data received'}), 400
    new_recipe_id = recipesDAO.create(data['name'], data['ingredients'], data['instructions'])
    logging.info(f"New recipe created with ID: {new_recipe_id}")
    return jsonify({'message': 'Recipe created successfully', 'recipe_id': new_recipe_id}), 201

@app.route('/api/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    logging.info(f"Accessing GET /api/recipes/{recipe_id} with recipe ID: {recipe_id}")
    recipe = recipesDAO.find_by_id(recipe_id)
    if recipe:
        return jsonify(recipe)
    else:
        abort(404)

@app.route('/api/recipes/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    logging.info(f"Accessing PUT /api/recipes/{recipe_id} with recipe ID: {recipe_id}")
    data = request.json
    logging.info(f"Received data: {data}")
    if not data or 'name' not in data or 'ingredients' not in data or 'instructions' not in data:
        logging.error("Invalid data received.")
        abort(400)
    recipesDAO.update(recipe_id, data['name'], data['ingredients'], data['instructions'])
    logging.info("Recipe updated successfully.")
    return jsonify({'message': 'Recipe updated successfully'})

@app.route('/api/recipes/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    logging.info(f"Accessing DELETE /api/recipes/{recipe_id} with recipe ID: {recipe_id}")
    recipesDAO.delete(recipe_id)
    logging.info("Recipe deleted successfully.")
    return jsonify({'message': 'Recipe deleted successfully'})

@app.route('/api/recipes/search', methods=['POST'])
def search_online_recipes():
    logging.info("Accessing POST /api/recipes/search...")
    data = request.json
    query = data.get('query')
    if not query:
        return jsonify({'error': 'Missing search query'}), 400
    
    api_response = recipesDAO.search_recipes_online(query)
    if api_response:
        recipes = api_response.get('hits', [])
        return jsonify(recipes)
    else:
        logging.error("Failed to fetch recipes from Edamam")
        return jsonify({'error': 'Failed to fetch recipes from Edamam'}), 500

@app.route('/api/recipes/add_online', methods=['POST'])
def add_online_recipes():
    logging.info("Accessing POST /api/recipes/add_online...")
    data = request.json
    query = data.get('query')
    if not query:
        return jsonify({'error': 'Missing search query'}), 400
    
    try:
        recipesDAO.add_online_recipe(query)
        return jsonify({'message': 'Recipes added successfully from Edamam'}), 201
    except Exception as e:
        logging.error(f"Error adding recipes from Edamam: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(threaded=True)
