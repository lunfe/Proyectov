from app import db
from sqlalchemy.orm import relationship

class Proveedores (db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    nombre= db.Column(db.String(255), nullable=False)
    contacto= db.Colum(db.String(255), nullable=False)
    telefono= db.Column(db.String(255), nullable=False)
    email= db.Colum(db.String(255), nullable=False)
    direccion= db.Colum(db.String(255), nullable=False)