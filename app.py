from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, Pet
from forms import AddPetForm

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
    pets = Pet.query.all()
    return render_template('homepage.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def show_add_pet_form():
    form = AddPetForm()
    if form.validate_on_submit():
        return redirect('/')
    else:
        return render_template('add_pet_form.html', form=form)
