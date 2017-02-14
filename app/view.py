from app import app
from flask import Flask, jsonify
import sqlmodel

@app.route("/<slug>")
def get_puppy(slug):
    result = sqlmodel.read(slug)
    index, name, full, url = result
    name, url = name.strip(), url.strip()
    output ={
        "name" : name,
        "image_url" : url,
    }
    return jsonify(output)
