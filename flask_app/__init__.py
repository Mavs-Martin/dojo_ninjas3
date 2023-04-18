from flask import Flask
app = Flask(__name__)
app.secret_key = "larc"
DATABASE = "dojos_and_ninja_schema"