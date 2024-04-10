"""Seed file to make sample data for the pet adoption agency database adopt_a_pet."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add pets
whiskey = Pet(name='Whiskey', species='dog', photo_url='https://image.petmd.com/files/styles/863x625/public/dog-allergies.jpg', age=4, notes='Do not actually give him Whiskey')
bowser = Pet(name='Bowser', species="porcupine", photo_url='https://brevardzoo.org/wp-content/uploads/2020/11/Shelley-2.jpg', age=2) 
franklin = Pet(name='Franklin', species="turtle", age=25, notes='No longer available for adoption', available=False)

# Add new objects to session, so they'll persist
db.session.add(whiskey)
db.session.add(bowser)
db.session.add(franklin)

# Commit -- otherwise, this never gets saved!
db.session.commit()

