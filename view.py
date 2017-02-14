from app import app
from flask import jsonify, abort
from app.model import db, Puppy
from flask_sqlalchemy import SQLAlchemy
import sys

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/puppydb'
db = SQLAlchemy(app)
p1 = Puppy(slug="rover", name="Rover",
           image_url="http://example.com/rover.jpg")
db.session.add(p1)
p2 = Puppy(slug="spot", name="Spot",
           image_url="http://example.com/spot.jpg")
db.session.add(p2)
db.session.commit()
print("Database seeded!")

@app.route("/<slug>")
def get_puppy(slug):
    puppy = Puppy.query.filter(Puppy.slug==slug).first_or_404()
    output ={
        "name" : puppy.name,
        "image_url" : puppy.image_url,
    }
    return jsonify(output)
