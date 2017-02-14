from app import app
from flask import jsonify, abort
from app.model import db, Puppy
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/puppydb'
db = SQLAlchemy(app)

@app.route("/<slug>")
def get_puppy(slug):
    
    output ={
        "name" : puppy.name,
        "image_url" : puppy.image_url,
    }
    return jsonify(output)
