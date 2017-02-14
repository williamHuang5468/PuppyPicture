from app import app
from flask import jsonify, abort

PUPPIES = [
    {
        "name" : "Rover",
        "image_url" : "http://example.com/rover.jpg",
    },
    {
        "name" : "Spot",
        "image_url" : "http://example.com/spot.jpg",
    },
]

@app.route("/<int:index>")
def get_puppy(index):
    try:
        puppy = PUPPIES[index]
    except IndexError:
        abort(404)
    return jsonify(puppy)
