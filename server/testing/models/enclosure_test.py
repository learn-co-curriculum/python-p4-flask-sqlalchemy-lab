from app import app, db
from server.models import Animal, Enclosure

class TestEnclosure:
    '''Enclosure model in models.py'''

    def test_can_be_instantiated(self):
        '''can be invoked to create a Python object.'''
        e = Enclosure()
        assert e
        assert isinstance(e, Enclosure)

    def test_has_environment_and_open_to_visitors(self):
        '''can be instantiated with an environment and open_to_visitors, a Boolean.'''
        e = Enclosure(environment='Desert', open_to_visitors=False)
        assert e.environment == 'Desert'
        assert e.open_to_visitors == False

    def test_can_be_saved_to_database(self):
        '''can be added to a transaction and committed to create a database record.'''
        with app.app_context():
            e = Enclosure()
            db.session.add(e)
            db.session.commit()
            assert hasattr(e, 'id')
            assert db.session.query(Enclosure).filter(Enclosure.id == e.id).one_or_none()

    def test_is_related_to_animals(self):
        '''has access to its associated animal objects.'''
        with app.app_context():
            a_1 = Animal()
            a_2 = Animal()
            e = Enclosure()
            db.session.add_all([a_1, a_2, e])
            db.session.commit()
            e.animals.append(a_1)
            e.animals.append(a_2)
            db.session.add(e)
            db.session.commit()
            assert e.animals == [a_1, a_2]
