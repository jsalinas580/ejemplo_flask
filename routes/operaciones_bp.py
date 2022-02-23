from flask import Blueprint
from controllers.Resta_Controller import resta_controler
from controllers.Suma_Controller import suma_controler

operaciones_bp = Blueprint('operaciones_bp', __name__)

operaciones_bp.route('/resta', methods=['POST', 'GET'])(resta_controler)
operaciones_bp.route('/suma', methods=['POST', 'GET'])(suma_controler)
