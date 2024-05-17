from flask import Blueprint, request, jsonify
from services.order_service import create_customer, create_order, update_order_status

order_bp = Blueprint('order', __name__)

@order_bp.route('/create', methods=['POST'])
def create_order_route():
    data = request.json
    customer_id = create_customer(data['customer_name'])
    order_id = create_order(customer_id, data['product_name'], data['quantity'], data['shop_owner'])
    return jsonify({'customer_id': customer_id, 'order_id': order_id}), 201

@order_bp.route('/update/<int:order_id>', methods=['PUT'])
def update_order_route(order_id):
    data = request.json
    updated_order = update_order_status(order_id, data['status'])
    if updated_order:
        return jsonify({'order_id': order_id, 'status': updated_order.status}), 200
    return jsonify({'error': 'Order not found'}), 404
