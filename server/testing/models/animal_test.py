from app import app, db
from server.models import Animal, Enclosure, Zookeeper

class TestAnimal:
    '''Animal model in models.py'''

    def test_can_be_instantiated(self):
        '''can be invoked to create a Python object.'''
        a = Animal()
        assert a
        assert isinstance(a, Animal)

    def test_has_name_and_species(self):
        '''can be instantiated with a name and species.'''
        a = Animal(name='Phil', species='Rhinoceros')
        assert a.name == 'Phil'
        assert a.species == 'Rhinoceros'

    def test_has_enclosure_id_and_zookeeper_id(self):
        '''has foreign keys for enclosure_id and zookeeper_id.'''
        a = Animal()
        assert hasattr(a, 'enclosure_id')
        assert hasattr(a, 'zookeeper_id')

    def test_can_be_saved_to_database(self):
        '''can be added to a transaction and committed to create a database record.'''
        with app.app_context():
            a = Animal()
            db.session.add(a)
            db.session.commit()
            assert hasattr(a, 'id')
            assert db.session.query(Animal).filter(Animal.id == a.id).one_or_none()

    def test_is_related_to_enclosures_and_zookeepers(self):
        '''has access to its associated enclosure and zookeeper objects.'''
        with app.app_context():
            a = Animal()
            e = Enclosure()
            z = Zookeeper()
            db.session.add_all([a, e, z])
            db.session.commit()
            a.enclosure_id = e.id
            a.zookeeper_id = z.id
            db.session.add(a)
            db.session.commit()
            assert a.enclosure == e
            assert a.zookeeper == z
