from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)  # Consider making this required
    image = db.Column(db.String, nullable=False)  # Consider making this required
    price = db.Column(db.Float, nullable=False)  # Consider making this required
    is_in_stock = db.Column(db.Boolean, default=True)  # Default value added

    def __repr__(self):
        return f'<Plant {self.name} | In Stock: {self.is_in_stock}>'
