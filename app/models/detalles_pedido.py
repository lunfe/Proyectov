from app import db
from sqlalchemy.orm import relationship

class Detalles_pedido (db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    cantidad= db.Column(db.String(255), nullable=False)
    precio_unitario= db.Colum(db.String(255), nullable=False)
    subtotal=db.Colum(db.String(255), nullable=False)
    pedidos_id = db.Column(db.Integer, db.ForeignKey('pedidos.id'))
    vinos_id = db.Column(db.Integer, db.ForeignKey('vinos.id'))