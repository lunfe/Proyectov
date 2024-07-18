from app import db
from sqlalchemy.orm import relationship

class Inventario (db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    cantidad= db.Column(db.String(255), nullable=False)
    fecha_actualizacion= db.Colum(db.String(255), nullable=False)
  