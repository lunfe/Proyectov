from flask import Blueprint
from app.routes import categorias_routes
from app.routes import clientes_routes
from app.routes import detalle_insumos_routes
from app.routes import detalles_pedido_routes
from app.routes import insumos_routes
from app.routes import inventario_routes
from app.routes import pedidos_routes
from app.routes import vinos_routes


bp = Blueprint('main', __name__)

