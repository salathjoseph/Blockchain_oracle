from flask import Flask
from models import db
from controllers.order_controller import order_bp
from controllers.tracking_controller import tracking_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(order_bp, url_prefix='/orders') ## post call
app.register_blueprint(tracking_bp, url_prefix='/tracking') ## Get call

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

