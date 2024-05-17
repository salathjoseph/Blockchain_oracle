from flask import Blueprint, jsonify
from services.order_service import get_order_status

tracking_bp = Blueprint('tracking', __name__)

@tracking_bp.route('/status/<int:order_id>', methods=['GET'])
def get_order_status_route(order_id):
    order_status = get_order_status(order_id)
    if order_status:
        return jsonify({'order_id': order_id, 'status': order_status}), 200
    return jsonify({'error': 'Order not found'}), 404
