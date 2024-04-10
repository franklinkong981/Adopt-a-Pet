from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, URLField

class AddPetForm(FlaskForm):
    """Form for adding a pet for adoption. The pet will be available by default.
    Users can enter a pet name, species, photo URL, age, and notes.
    Validation: Species is required, must be cat dog porcupine or turtle, pet name is required, photo URL must be in URL format,
    age must be between 0 and 30."""

    name = StringField("Pet name")
    species = SelectField("Species", choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine'), ('turtle', 'Turtle')])
    photo_url = URLField("Photo URL")
    age = IntegerField("Age of pet")
    notes = StringField("Additional Notes")
