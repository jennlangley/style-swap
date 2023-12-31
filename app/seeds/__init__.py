from flask.cli import AppGroup
from .users import seed_users, undo_users
from .category import seed_categories, undo_categories
from .product import seed_products, undo_products
from .image import seed_images, undo_images
from .review import seed_reviews, undo_reviews
from .order import seed_orders, undo_orders
from .product_category import seed_products_categories, undo_products_categories
from .follow import seed_follows, undo_follows

from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo 
        # command, which will  truncate all tables prefixed with 
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_users()
        undo_products()
        undo_images()
        undo_categories()
        undo_products_categories()
        undo_reviews()
        undo_orders()
        undo_follows()
        
        
        
    seed_users()
    # Add other seed functions here
    seed_products()
    seed_images()
    seed_categories()
    seed_products_categories()
    seed_reviews()
    seed_orders()
    seed_follows()
    
    


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    # Add other undo functions here
    undo_categories()
    undo_products_categories()
    undo_products()
    undo_images()
    undo_reviews()
    undo_orders()
    undo_follows()