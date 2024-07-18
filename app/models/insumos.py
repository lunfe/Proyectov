from app import db
from sqlalchemy.orm import relationship

class Insumos (db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    nombre= db.Column(db.String(255), nullable=False)
    descipcion= db.Colum(db.String(255), nullable=False)
    precio= db.Colum(db.String(255), nullable=False)
    provedores_id = db.Column(db.Integer, db.ForeignKey('proveedores.id'))