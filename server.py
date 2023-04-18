from flask_app import app
from flask_app.controllers import dojos_cont, ninjas_cont


#used to test if pasge was working and yes it is

if __name__=="__main__":
    app.run(debug=True, port=5001)