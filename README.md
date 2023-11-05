# Flask-SQLAlchemy Lab

## Learning Goals

- Build and run a Flask application on your computer.
- Extend a Flask application to meet the unique requirements of different
  projects.

---

## Key Vocab

- **Web Framework**: software that is designed to support the development of web
  applications. Web frameworks provide built-in tools for generating web
  servers, turning Python objects into HTML, and more.
- **Extension**: a package or module that adds functionality to a Flask
  application that it does not have by default.
- **Request**: an attempt by one machine to contact another over the internet.
- **Client**: an application or machine that accesses services being provided by
  a server through the internet.
- **Web Server**: a combination of software and hardware that uses Hypertext
  Transfer Protocol (HTTP) and other protocols to respond to requests made over
  the internet.
- **Web Server Gateway Interface (WSGI)**: an interface between web servers and
  applications.
- **Template Engine**: software that takes in strings with tokenized values,
  replacing the tokens with their values as output in a web browser.

---

## Instructions

This is a **test-driven lab**. Run `pipenv install` to create your virtual
environment and `pipenv shell` to enter the virtual environment. Then run
`pytest -x` to run your tests. Use these instructions and `pytest`'s error
messages to complete your work in the `server/` folder.

Instructions begin here:

- Design a Flask application that displays information from a database created
  using Flask-SQLAlchemy and Flask-Migrate.
- `flask db init` has already been run. You will need to direct your Flask app
  to a database at `app.db`, create models, run a migration with
  `flask db revision --autogenerate -m'<your message>'` and create the database
  file with `flask db upgrade`.
- Your database should represent a zoo. There should be three tables: `animals`,
  `zookeepers`, and `enclosures`.
- The `Animal` model should contain a String `name`, a String `species`, a
  `zookeeper_id`, and an `enclosure_id`. It should be related to zookeepers and
  enclosures using `db.relationship()`.
  - _Reminder: You can test any model by itself with
    `pytest testing/models/{modelname}_test.py`._
- The `Zookeeper` model should contain a String `name`, a String `birthday`, and
  a list of `animals` that they take care of using `db.relationship()`.
- The `Enclosure` model should contain a String `environment` (grass, sand, or
  water), a Boolean `open_to_visitors`, and a list of `animals` using
  `db.relationship()`.
- Your application should contain three views: `animal_by_id`,
  `zookeeper_by_id`, and `enclosure_by_id`. Their routes should be
  `animal/<int:id>`, `zookeeper/<int:id>`, and `enclosure/<int:id>`,
  respectively.
- Each view should display all attributes as line items (`ul`). If there is a
  one-to-many relationship, each of the many should have its own line item.
- A seed script, `server/seed.py`, has been provided to generate test data once
  your models have been built and migrated to a database. Make sure to run this
  so that there are resources for the test suite to visit.

Once all of your tests are passing, commit and push your work using `git` to
submit.

### Examples

#### Animal View

![animal ID 1, name Logan, species Snake, zookeeper Dylan Taylor,
enclosure trees](https://curriculum-content.s3.amazonaws.com/python/flask-sqlalchemy-lab-1.png)

#### Zookeeper View

![zookeeper name Stephanie Contreras, birthday 1996-9-20, 6 animals](https://curriculum-content.s3.amazonaws.com/python/flask-sqlalchemy-lab-2.png)

#### Enclosure View

![enclosure with pond environment, not open to visitors, 8 animals](https://curriculum-content.s3.amazonaws.com/python/flask-sqlalchemy-lab-3.png)

---

## Resources

- [Quickstart - Flask-SQLAlchemy][flask_sqla]
- [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)
- [Flask Extensions, Plug-ins, and Related Libraries - Full Stack Python](https://www.fullstackpython.com/flask-extensions-plug-ins-related-libraries.html)

[flask_sqla]: https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#
