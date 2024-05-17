from flask import Flask
from models import db
from controllers.order_controller import order_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(order_bp, url_prefix='/orders')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
