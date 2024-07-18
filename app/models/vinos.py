from app import db
from sqlalchemy.orm import relationship

class Vinos (db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    nombre= db.Column(db.String(255), nullable=False)
    descripcion= db.Colum(db.String(255), nullable=False)
    precio=db.Colum(db.String(255), nullable=False)
    stock= db.Colum(db.string(255), nullable=False)
    categorias_id = db.Column(db.Integer, db.ForeignKey('categorias.id'))
    inventario_id = db.Column(db.Integer, db.ForeignKey('inventario.id'))