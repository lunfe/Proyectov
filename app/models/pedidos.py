from app import db
from sqlalchemy.orm import relationship

class Pedidos (db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    fecha_pedido= db.Column(db.String(255), nullable=False)
    total= db.Colum(db.String(255), nullable=False)
    clientes_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))