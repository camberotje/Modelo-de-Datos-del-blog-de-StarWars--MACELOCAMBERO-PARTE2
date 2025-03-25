from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class Characters (db.Model):
    __tablename__ = 'Characters'  

    character_id = Column(Integer, ForeignKey("Favorites.character_id") primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    height = Column(Integer, nullable=False) 
    date_of_birth = Column(Date, nullable=False)  
    gender = Column(String(20), nullable=False) 

    conection_favorites = relationship("Favorites", back_populates="conection_characters")
    

    def serialize(self):
        return {
        "character_id": self.character_id,
        "name": self.name,
        "height": self.height, 
        "date_of_birth": self.date_of_birth,  
        "gender": self.gender
        }
    

class vehicles (db.Model):
    __tablename__ = 'Vehicles'  

    vehicles_id = Column(Integer, ForeignKey("Favorites.vehicle_id") primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    model = Column(String, nullable=False) 
    manufacturer = Column(String(50), nullable=False) 
    length = Column(Integer, nullable=False) 
    max_speed = Column(Integer, nullable=False)

    conection_favorites2 = relationship("Favorites", back_populates="conection_vehicles")

    
    def serialize(self):
        return {
        "vehicles_id": self.vehicles_id,
        "name": self.name,
        "model": self.model, 
        "manufacturer": self.manufacturer, 
        "length": self.length,  
        "max_speed": self.max_speed  
        }
    
class Species (db.Model):
    __tablename__ = 'Species'  

    specie_id = Column(Integer, ForeignKey("Favorites.specie_id") primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    classification = Column(String(50), nullable=False) 
    average_height = Column(Integer, nullable=False) 
    language = Column(String(50), nullable=False) 
    homeworld = Column(String(50), nullable=True)

    conection_favorites3 = relationship("Species", back_populates="conection_species")

    
    def serialize(self):
        return {
       "specie_id": self.specie_id,
        "name": self.name,
        "classification": self.classification, 
        "average_height": self.average_height, 
        "language": self.language, 
        "homeworld": self.homeworld 
         }
    
    class Planets (db.Model):
        __tablename__ = 'Planets'  

    planet_id = Column(Integer, ForeignKey("Favorites.planet_id") primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    diameter = Column(Integer, nullable=False) 
    rotation_period = Column(Integer, nullable=False) 
    gravity = Column(String(50), nullable=False) 
    population = Column(Integer, nullable=True)

    conection_favorites4 = relationship("Planets", back_populates="conection_planets")

    
    def serialize(self):
        return {
        "planet_id": self.planet_id,
        "name": self.name,
        "diameter": self.diameter,
        "rotation_period": self.rotation_period,
        "gravity": self.gravity,
        "population": self.population
         }
    
    class Favorites (db.Model):
        __tablename__ = 'Favorites'  
    
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, primary_key=True)
    specie_id = Column(Integer, primary_key=True)
    vehicle_id = Column(Integer, primary_key=True)
    character_id = Column(Integer, primary_key=True)

    conection_characters = relationship("Character", back_populates="conection_favorites")
    conection_vehicles = relationship("vehicles", back_populates="conection_favorites2")
    conection_species = relationship("Species", back_populates="conection_favorites3")
    conection_planets = relationship("Planets", back_populates="conection_favorites4")
    conection_users = relationship("User", back_populates="conection_favorites5")

    def serialize(self):
        return {
        "planet_id": self.planet_id,
        "specie_id": self.specie_id,
        "vehicle_id": self.vehicle_id,
        "character_id": self.character_id
         }
    
    class User (db.Model):
        __tablename__ = 'User'  
    
    user_id = Column(Integer, ForeignKey("Favorites.id") primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

    conection_favorites5 = relationship("User", back_populates="conection_favorites5")

    def serialize(self):
        return {
        "planet_id": self.planet_id,
        "specie_id": self.specie_id,
        "vehicle_id": self.vehicle_id,
        "character_id": self.character_id
         }
    

    



    
    

