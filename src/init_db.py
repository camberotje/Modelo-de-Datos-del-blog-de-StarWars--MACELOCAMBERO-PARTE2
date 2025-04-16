import os
from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from models import db, User, Characters, Vehicles, Species, Planets, Favorites
from load_initial_data import load_initial_data

"""
Este script inicializa la base de datos y carga datos iniciales.
Usa una configuración similar a la de app.py para mantener coherencia.
"""

# Configuración de la aplicación Flask
app = Flask(__name__)
app.url_map.strict_slashes = False

# Usar la misma configuración de base de datos que en app.py
db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)

if __name__ == "__main__":
    with app.app_context():
        # Crear todas las tablas
        print("Creando tablas en la base de datos...")
        db.create_all()
        
        # Cargar los datos iniciales
        print("Iniciando carga de datos...")
        load_initial_data()
        
        print("¡Proceso completado!")