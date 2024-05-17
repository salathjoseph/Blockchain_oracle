from models import db, Customer, Order

def create_customer(name):
    customer = Customer(name=name)
    db.session.add(customer)
    db.session.commit()
    return customer.id

def create_order(customer_id, product_name, quantity, shop_owner):
    order = Order(customer_id=customer_id, product_name=product_name, quantity=quantity, shop_owner=shop_owner)
    db.session.add(order)
    db.session.commit()
    return order.id

def update_order_status(order_id, status):
    order = Order.query.get(order_id)
    if order:
        order.status = status
        db.session.commit()
        return order
    return None
