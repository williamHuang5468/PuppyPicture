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

PUPPIES = {
    "rover":{
        "name" : "Rover",
        "image_url" : "http://example.com/rover.jpg",
    },
    "spot":{
        "name" : "Spot",
        "image_url" : "http://example.com/spot.jpg",
    },
}

@app.route("/<slug>")
def get_puppy(slug):
    try:
        puppy = PUPPIES[slug]
    except KeyError:
        abort(404)
    return jsonify(puppy)
