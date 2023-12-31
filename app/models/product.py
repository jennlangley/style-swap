from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Product(db.Model):
    __tablename__ = 'products'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    condition = db.Column(db.String(40), nullable=False)
    size = db.Column(db.String(40), nullable=False)
    price = db.Column(db.Numeric(precision=2), nullable=False)
    sold = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())

    user = db.relationship("User", back_populates="products")
    review = db.relationship("Review", uselist=False, back_populates="product")
    category = db.relationship("ProductCategory", uselist=False, back_populates="products", cascade="all, delete")
    images = db.relationship("Image", back_populates="product", cascade="all, delete")
    order = db.relationship("Order", uselist=False, back_populates="product")

    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.user_id,
            'user': self.user.to_dict(),
            'name': self.name,
            'desc': self.desc,
            'condition': self.condition,
            'size': self.size,
            'price': round(self.price, 2),
            'sold': self.sold,
            'categoryId': self.category.categories.to_dict()['categoryId'],
            'subcategoryId': self.category.categories.to_dict()['id'],
            'images': [image.to_dict() for image in self.images],
            'createdAt': self.created_at.strftime("%m/%d/%Y"),
            'updatedAt': self.updated_at.strftime("%m/%d/%Y"),
        }
