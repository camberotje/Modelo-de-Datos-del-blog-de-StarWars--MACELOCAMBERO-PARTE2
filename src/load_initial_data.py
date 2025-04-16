from models import db, User, Characters, Vehicles, Species, Planets, Favorites
from datetime import date

def load_initial_data():
    """
    Función para cargar datos iniciales en la base de datos.
    Ejecuta este script después de crear todas las tablas con db.create_all()
    """
    # Verificar si ya hay datos en la base de datos
    if User.query.count() > 0:
        print("La base de datos ya tiene datos. Saltando la inicialización.")
        return
    
    print("Cargando datos iniciales...")
    
    # Crear usuarios de ejemplo con contraseñas en texto plano
    users = [
        User(
            username="luke_skywalker", 
            email="luke@rebellion.org", 
            password="usetheforce"
        ),
        User(
            username="darth_vader", 
            email="vader@empire.gov", 
            password="iamyourfather"
        ),
        User(
            username="leia_organa", 
            email="leia@rebellion.org", 
            password="alderaan"
        )
    ]
    
    # Agregar usuarios a la sesión
    for user in users:
        db.session.add(user)
    
    # Crear planetas
    planets = [
        Planets(
            name="Tatooine",
            diameter=10465,
            rotation_period=23,
            gravity="1 standard",
            population=200000
        ),
        Planets(
            name="Alderaan",
            diameter=12500,
            rotation_period=24,
            gravity="1 standard",
            population=2000000000
        ),
        Planets(
            name="Coruscant",
            diameter=12240,
            rotation_period=24,
            gravity="1 standard",
            population=1000000000000
        ),
        Planets(
            name="Dagobah",
            diameter=8900,
            rotation_period=23,
            gravity="N/A",
            population=None
        ),
        Planets(
            name="Endor",
            diameter=4900,
            rotation_period=18,
            gravity="0.85 standard",
            population=30000000
        )
    ]
    
    # Agregar planetas a la sesión
    for planet in planets:
        db.session.add(planet)
    
    # Crear especies
    species = [
        Species(
            name="Human",
            classification="mammal",
            average_height=180,
            language="Galactic Basic",
            homeworld="Coruscant"
        ),
        Species(
            name="Wookiee",
            classification="mammal",
            average_height=210,
            language="Shyriiwook",
            homeworld="Kashyyyk"
        ),
        Species(
            name="Hutt",
            classification="gastropod",
            average_height=300,
            language="Huttese",
            homeworld="Nal Hutta"
        ),
        Species(
            name="Yoda's species",
            classification="unknown",
            average_height=66,
            language="Galactic Basic",
            homeworld=None
        ),
        Species(
            name="Ewok",
            classification="mammal",
            average_height=100,
            language="Ewokese",
            homeworld="Endor"
        )
    ]
    
    # Agregar especies a la sesión
    for specie in species:
        db.session.add(specie)
    
    # Crear vehículos
    vehicles = [
        Vehicles(
            name="X-wing",
            model="T-65 X-wing",
            manufacturer="Incom Corporation",
            length=12,
            max_speed=1050
        ),
        Vehicles(
            name="Millennium Falcon",
            model="YT-1300 light freighter",
            manufacturer="Corellian Engineering Corporation",
            length=34,
            max_speed=1050
        ),
        Vehicles(
            name="TIE Fighter",
            model="Twin Ion Engine Fighter",
            manufacturer="Sienar Fleet Systems",
            length=6,
            max_speed=1200
        ),
        Vehicles(
            name="Speeder Bike",
            model="74-Z speeder bike",
            manufacturer="Aratech Repulsor Company",
            length=3,
            max_speed=360
        ),
        Vehicles(
            name="AT-AT",
            model="All Terrain Armored Transport",
            manufacturer="Kuat Drive Yards",
            length=20,
            max_speed=60
        )
    ]
    
    # Agregar vehículos a la sesión
    for vehicle in vehicles:
        db.session.add(vehicle)
    
    # Crear personajes
    characters = [
        Characters(
            name="Luke Skywalker",
            height=172,
            date_of_birth=date(19, 5, 16),  # 19 BBY en universo Star Wars
            gender="male"
        ),
        Characters(
            name="Darth Vader",
            height=202,
            date_of_birth=date(41, 5, 16),  # 41 BBY en universo Star Wars
            gender="male"
        ),
        Characters(
            name="Leia Organa",
            height=150,
            date_of_birth=date(19, 5, 16),  # 19 BBY en universo Star Wars
            gender="female"
        ),
        Characters(
            name="Han Solo",
            height=180,
            date_of_birth=date(29, 7, 16),  # 29 BBY en universo Star Wars
            gender="male"
        ),
        Characters(
            name="Yoda",
            height=66,
            date_of_birth=date(896, 1, 1),  # 896 BBY en universo Star Wars
            gender="male"
        )
    ]
    
    # Agregar personajes a la sesión
    for character in characters:
        db.session.add(character)
    
    # Realizar commit para guardar los datos anteriores y poder acceder a sus ids
    db.session.commit()
    
    # Crear favoritos para los usuarios
    # Nota: Ahora podemos acceder a los ids de los elementos creados anteriormente
    
    # Favoritos para Luke Skywalker
    favorites_luke = [
        Favorites(
            user_id=users[0].id,
            planet_id=planets[0].id,  # Tatooine
            character_id=characters[3].id,  # Han Solo
            vehicle_id=vehicles[0].id,  # X-wing
            specie_id=species[1].id  # Wookiee
        ),
        Favorites(
            user_id=users[0].id,
            planet_id=planets[3].id,  # Dagobah
            character_id=characters[4].id,  # Yoda
            vehicle_id=None,
            specie_id=None
        )
    ]
    
    # Favoritos para Darth Vader
    favorites_vader = [
        Favorites(
            user_id=users[1].id,
            planet_id=planets[2].id,  # Coruscant
            character_id=None,
            vehicle_id=vehicles[2].id,  # TIE Fighter
            specie_id=None
        ),
        Favorites(
            user_id=users[1].id,
            planet_id=None,
            character_id=characters[0].id,  # Luke Skywalker
            vehicle_id=None,
            specie_id=None
        )
    ]
    
    # Favoritos para Leia Organa
    favorites_leia = [
        Favorites(
            user_id=users[2].id,
            planet_id=planets[1].id,  # Alderaan
            character_id=characters[3].id,  # Han Solo
            vehicle_id=vehicles[1].id,  # Millennium Falcon
            specie_id=None
        )
    ]
    
    # Agregar todos los favoritos a la sesión
    for favorite in favorites_luke + favorites_vader + favorites_leia:
        db.session.add(favorite)
    
    # Realizar commit final para guardar todos los datos
    db.session.commit()
    
    print("Datos iniciales cargados con éxito!")


if __name__ == "__main__":
    # Este script debe ser importado y llamado desde otro archivo
    # que ya tenga el contexto de la aplicación Flask
    pass