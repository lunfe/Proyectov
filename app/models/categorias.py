from app import db
from sqlalchemy.orm import relationship

class Categorias (db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    nombre = db.Column(db.String(255), nullable=False)
    descripcion = db.colum(db.String(255), nullable=False)
