from app.models import db, Product, environment, SCHEMA
from sqlalchemy.sql import text


def seed_products():
    product_1 = Product(
        name="Women's Blue Jeans", user_id=1,
        desc="High quality blue jeans, perfect for all seasons!", condition="Used - Good", 
        size="S", price=15.00, sold=False,
    )
    product_2 = Product(
        name="Yellow Sweater", user_id=2,
        desc="Vintage sweater, great condition very comfortable and warm material", 
        condition="Used - Excellent", 
        size="L", price=32.00, sold=True,
    )
    product_3 = Product(
        name="Men's Blue Jeans", user_id=2,
        desc="Vintage jeans from the 80s-90s", condition="Used - Excellent", 
        size="M", price=25.00, sold=False,
    )
    product_4 = Product(
        name="Women's Dress", user_id=1,
        desc="Formal silky womens dress, worn once, great for special occasions", 
        condition="Like new", 
        size="S", price=30.00, sold=False,
    )
    product_5 = Product(
        name="Men's hat", user_id=3,
        desc="Black SnapBack Hat", condition="Used - Fair", 
        size="L", price=8.00, sold=False,
    )
    product_6 = Product(
        name="Vintage Watch", user_id=1,
        desc="Special edition vintage watch, one of a kind", condition="Used - Good", 
        size="M", price=60.00, sold=True,
    )
    product_7 = Product(
        name="White sneakers", user_id=1,
        desc="crisp and clean white sneakers, worn once, great price buy now!", condition="Used - Excellent", 
        size="L", price=14.99, sold=True,
    )
    product_8 = Product(
        name="Classic Earrings", user_id=2,
        desc="your standard ear rings, found in packaging at estate sale, one of a kind piece", condition="Brand new", 
        size="S", price=30.00, sold=True,
    )
    # product_9 = Product(
    #     name=, user_id=,
    #     desc=, condition="Used - Fair", 
    #     size="", price=, sold=False,
    # )
    # product_10 = Product(
    #     name=, user_id=,
    #     desc=, condition="Like new", 
    #     size="", price=, sold=False,
    # )

    db.session.add(product_1)
    db.session.add(product_2)
    db.session.add(product_3)
    db.session.add(product_4)
    db.session.add(product_5)
    db.session.add(product_6)
    db.session.add(product_7)
    db.session.add(product_8)
    # db.session.add(product_9)
    # db.session.add(product_10)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_products():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.products RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM products"))
        
    db.session.commit()