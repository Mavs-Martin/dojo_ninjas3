from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo_mod import Dojo
from flask_app.models.ninja_mod import Ninja


#takes me to the new dojo/ all dojo page 5001 tested
@app.route('/')
def index():
    dojos = Dojo.get_all()    
    return render_template('dojo.html', all_dojos=dojos)

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template("dojoshow", all_dojos=dojos)

@app.route('/create/dojo',methods=['POST'])
def create():
    print(request.form)
    Dojo.create_location(request.form)
    return redirect('/')

@app.route('/dojo/<int:id>')
def show(id):
    data = {
        "id":id
    }
    dojos = Dojo.get_one(data)
    ninjas = Ninja.get_all()
    return render_template("dojo_show.html", ninjas = ninjas, dojo = dojos)


