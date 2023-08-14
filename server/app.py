#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.filter(Animal.id == id).first()
    # looking through Zookeeper.id to find the same ID in Animal
    zookeeper = Zookeeper.query.filter(Zookeeper.id == animal.zookeeper_id).first()
    enclosure = Enclosure.query.filter(Enclosure.id == animal.enclosure_id).first()
    response_body =  f'''<ul>{animal.id}
    <ul>Name: {animal.name}</ul>
    <ul>Species: {animal.species}</ul>
    <ul>Zookeeper Name:{zookeeper.name}</ul>
    <ul>Enclosure: {enclosure.environment}</ul>'''
    if not animal:
        response_body = "<h1>404 No Animals Found</h1>"
        response = make_response(response_body,404)
        return response
    
    response = make_response(response_body,200)
    return response

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.filter(Zookeeper.id == id).first()
    response_body = f'<ul>Name:{zookeeper.name}</ul>'
    response_body += f'<ul>Birthday: {zookeeper.birthday}</ul>'
    animals = [pet for pet in zookeeper.animals]
    if not animals:
        response_body += f'<ul>No animals</ul>'
    else:
        for animal in zookeeper.animals:
            response_body += f'<ul>Animal: {animal.name}</ul>'
    response = make_response(response_body, 200)
    return response

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.filter(Enclosure.id == id).first()
    response_body = f'<ul>Environment:{enclosure.environment}</ul>'
    response_body += f'<ul>Open to Visitors:{enclosure.open_to_visitors}</ul>'
    animals = [pet for pet in enclosure.animals]
    if not animals:
        response_body += '<ul>No animals in this environment</ul>'
    else:
        for pet in enclosure.animals:
            response_body += f'<ul>Animal: {pet.name}</ul>'
    response = make_response(response_body, 200)
    return response


if __name__ == '__main__':
    app.run(port=5555, debug=True)
