from app import db
from sqlalchemy.orm import relationship

class Clientes (db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    nombre = db.Column(db.String(255), nullable=False)
    apellido= db.colum(db.String(255), nullable=False)
    email=db.colum(db.String(255), nullable=False)
    direccion=db.colum(db.String(255), nullable=False)
    telefono=db.colum(db.String(255), nullable=False)
  