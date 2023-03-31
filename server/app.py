#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate
from flask_debugtoolbar import DebugToolbarExtension

import os
from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "123456" #os.getenv("SECRET_KEY")
app.debug = True

toolbar = DebugToolbarExtension(app)
migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<body><h1>Zoo app</h1></body>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.filter(Animal.id == id).first()
    
    if not animal:
        response_text = "<body><h1>The animal you look for does not seem to exist!</h1></body>"
        response = make_response(response_text, 404)
        return response
    
    response_text = f"""
        <body>
            <ul>ID: {animal.id}</ul>
            <ul>Name: {animal.name}</ul>
            <ul>Species: {animal.species}</ul>
            <ul>Zookeeper: {animal.zookeeper.name}</ul>
            <ul>Enclosure: {animal.enclosure.environment}</ul>
        </body>
    """
    response = make_response(response_text, 200)
    return response

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.filter(Zookeeper.id == id).first()
    
    if not zookeeper:
        response_text = "<body><h1>The zookeeper you look for does not seem to exist!</h1></body>"
        response = make_response(response_text, 404)
        return response
    
    response_text = f"""
        <body>
            <ul>ID: {zookeeper.id}</ul>
            <ul>Name: {zookeeper.name}</ul>
            <ul>Birthday: {zookeeper.birthday}</ul>
            {"".join([f"<ul>Animal: {animal.name}</ul>" for animal in zookeeper.animals])}
        </body>
    """
    response = make_response(response_text, 200)
    return response

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.filter(Enclosure.id == id).first()
    
    if not enclosure:
        response_text = "<body><h1>The enclosure you look for does not seem to exist!</h1></body>"
        response = make_response(response_text, 404)
        return response
    
    response_text = f"""
        <body>
            <ul>ID: {enclosure.id}</ul>
            <ul>Environment: {enclosure.environment}</ul>
            <ul>Open to Visitors: {enclosure.open_to_visitors}</ul>
            {"".join([f"<ul>Animal: {animal.name}</ul>" for animal in enclosure.animals])}
        </body>
    """
    response = make_response(response_text, 200)
    return response


if __name__ == '__main__':
    app.run(port=5555, debug=True)
