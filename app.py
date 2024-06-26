from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_a_pet'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
app.app_context().push()

@app.route('/')
def list_pets():
    """Shows the homepage which lists all the pets and shows their photos, names, and whether they're available."""
    available_pets = Pet.query.filter(Pet.available == True)
    unavailable_pets = Pet.query.filter(Pet.available == False)
    return render_template('homepage.html', available_pets=available_pets, unavailable_pets=unavailable_pets)

@app.route('/add', methods=['GET', 'POST'])
def show_add_pet_form():
    """If it's not a POST request being sent to this route OR the form isn't validated, shows the add new pet form. Otherwise, processes the form,
    adds the new pet to the adopt_a_pet database, and redirects to the home page."""
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data if form.photo_url.data else None
        age = form.age.data if form.age.data else None
        notes = form.notes.data if form.notes.data else None

        new_pet = Pet(name=name,species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        flash('Pet successfully added!')
        return redirect('/')
    else:
        return render_template('add_pet_form.html', form=form)

@app.route('/<int:pet_id_number>', methods=['GET', 'POST'])
def show_pet_details_page(pet_id_number):
    """If it's a GET request, display detailed pet information such as the name, species, photo, age, and notes, if present."""
    pet_to_update = Pet.query.get_or_404(pet_id_number)
    form = EditPetForm(obj=pet_to_update)
    if form.validate_on_submit():
        pet_to_update.photo_url = form.photo_url.data if form.photo_url.data else None
        pet_to_update.age = form.age.data if form.age.data else None
        pet_to_update.notes = form.notes.data if form.notes.data else None
        pet_to_update.available = form.available.data

        db.session.commit()
        flash('Pet successfully updated!')
        return redirect(f'/{pet_id_number}')
    else:
        return render_template('edit_pet_form.html', form=form, pet=pet_to_update)

