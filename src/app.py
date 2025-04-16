"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planets
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

## Vamos a crear una ruta para traernos todos los planetas y 1 solo planeta (Vamos a usar dos serialize diferentes)

@app.route('/planets', methods=['GET'])
def get_all_planets():
    
    # Buscamos todos los planetas en la base de datos y guardamos esta búsqueda en la variable planets
    planets = Planets.query.all()
    
    # Comprobamos que hemos encontrado algún planeta
    if not planets:
        return jsonify({'msg' : 'Not able to find any planets'}), 404
    
    # Serializamos con el método serialize_for_all los planetas que hayamos encontrado
    planets_serialized = [planet.serialize_for_all() for planet in planets]
    
    # Jsonificamos el objeto para mandar al frontend
    return jsonify({
        'msg' : 'We find some planets',
        'planets' : planets_serialized}), 200
    
@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_a_planet(planet_id):
    
    planet = Planets.query.get(planet_id)
    
    
    # Comprobamos que hemos encontrado algún planeta
    if not planet:
        return jsonify({'msg' : 'Not able to find any planets'}), 404
    
    # Jsonificamos el objeto para mandar al frontend
    return jsonify({
        'msg' : 'We find the planet',
        'planet' : planet.serialize_for_one()}), 200
    
    
    
    
    
    
    
    
    # Vamos a buscar todos los favoritos de un usuario (user_id_route porque vendrá de la ruta)
    # user_favorites = Favorites.query.filter(Favorites.user_id == user_id_route).all()
    # Ahora tendremos que serializar (Tenemos que hacer algo muy muy muy parecido al serialize de get_all_planets)
    
    
    



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
