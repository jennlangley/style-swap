from app.models import db, Order, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_orders():
    order_1 = Order(
        product_id=6, user_id=2, review_id=1
    )
    order_2 = Order(
        product_id=7, user_id=2, review_id=2
    )
    order_3 = Order(
        product_id=8, user_id=1, review_id=3
    )
    order_4 = Order(
        product_id=2, user_id=1,
    )
    order_5 = Order(
        product_id=3, user_id=1
    )
    # order_4 = Order(
    #     product_id=,user_id=
    # )
    # order_5 = Order(
    #     product_id=,user_id=
    # )

    db.session.add(order_1)
    db.session.add(order_2)
    db.session.add(order_3)
    db.session.add(order_4)
    db.session.add(order_5)
    # db.session.add(order_4)
    # db.session.add(order_5)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_orders():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.orders RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM orders"))
        
    db.session.commit()