from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, URLField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    """Form for adding a pet for adoption. The pet will be available by default.
    Users can enter a pet name, species, photo URL, age, and notes.
    Validation: Species is required, must be cat dog porcupine or turtle, pet name is required, photo URL must be in URL format,
    age must be between 0 and 30."""

    name = StringField("Pet name", validators=[InputRequired(message="You must provide a name for the pet!")])
    species = SelectField("Species", choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine'), ('turtle', 'Turtle')], validators=[InputRequired(message="Please provide a species name.")])
    photo_url = URLField("Photo URL", validators=[Optional(), URL(message="The Photo URL must be a valid URL!")])
    age = IntegerField("Age of pet", validators=[Optional(), NumberRange(min=0, max=30, message="The age of the pet must be an integer between 0 and 30!")])
    notes = StringField("Additional Notes", validators=[Optional()])

class EditPetForm(FlaskForm):
    """Form for updating an existing pet's information. Users can update the pet's photo URL, notes, and whether the pet is 
    available or not."""

    photo_url = URLField("Photo URL", validators=[Optional(), URL(message="The Photo URL must be a valid URL!")])
    age = IntegerField("Age of pet", validators=[Optional(), NumberRange(min=0, max=30, message="The age of the pet must be an integer between 0 and 30!")])
    notes = StringField("Additional Notes", validators=[Optional()])
    available = BooleanField("Is pet available")

