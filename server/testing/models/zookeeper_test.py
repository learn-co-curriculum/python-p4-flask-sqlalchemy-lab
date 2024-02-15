from app import app, db
from server.models import Animal, Zookeeper

class TestZookeeper:
    '''Zookeeper model in models.py'''

    def test_can_be_instantiated(self):
        '''can be invoked to create a Python object.'''
        z = Zookeeper()
        assert z
        assert isinstance(z, Zookeeper)

    def test_has_environment_and_open_to_visitors(self):
        '''can be instantiated with a name and birthday.'''
        z = Zookeeper(name='Steve Irwin', birthday='02/22/1962')
        assert z.name == 'Steve Irwin'
        assert z.birthday == '02/22/1962'

    def test_can_be_saved_to_database(self):
        '''can be added to a transaction and committed to create a database record.'''
        with app.app_context():
            z = Zookeeper()
            db.session.add(z)
            db.session.commit()
            assert hasattr(z, 'id')
            assert db.session.query(Zookeeper).filter(Zookeeper.id == z.id).one_or_none()

    def test_is_related_to_animals(self):
        '''has access to its associated animal objects.'''
        with app.app_context():
            a_1 = Animal()
            a_2 = Animal()
            z = Zookeeper()
            db.session.add_all([a_1, a_2, z])
            db.session.commit()
            z.animals.append(a_1)
            z.animals.append(a_2)
            db.session.add(z)
            db.session.commit()
            assert z.animals == [a_1, a_2]
