from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.ninja_mod import Ninja
from flask_app.models.dojo_mod import Dojo

@app.route('/ninja')
def ninja():
    dojos = Dojo.get_all()
    return render_template('ninja.html', dojos = dojos)

@app.route('/create/ninja', methods= ["POST"])
def create_ninja():
    Ninja.save(request.form)
    return redirect('/')