from app import db
from sqlalchemy.orm import relationship

class Detalle_insumos (db.Model):
  
    vinos_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    insumos_id= db.Colum(db.Integer, db.ForeignKey('insumos.id'))
