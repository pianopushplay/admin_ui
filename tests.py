from flask_testing import TestCase
import unittest
from flask_login import current_user

from app import app, db, bcrypt
from models import User, Role, Piano


class BaseTestCase(TestCase):
    """A base test case."""

    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.add(User(first_name="admin", last_name="admin",
                            email="admin@gmail.com", password="pianoadmin",
                            roles=[Role(name="superuser", description="can do anything")])
                       )
        db.session.add(Piano(title="test@pdx", lon=123.56, lat=458.122))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class FlaskTestCase(BaseTestCase):

    # Ensure that Flask was set up correctly
    def test_index(self):
        response = self.client.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Go to admin!', response.data)


    # Ensure that main page requires user login
    def test_main_route_requires_login(self):
        response = self.client.get('/admin/', follow_redirects=True)
        self.assertIn(b'Please log in', response.data)



class TestUser(BaseTestCase):
    # Ensure a logged in superuser can create a volunteer with volunteer role
    def test_superuser_can_create_voluntteer(self):
        with self.client:
            self.client.post(
                '/admin/login/',
                data=dict(email="admin@gmail", password="pianoadmin"),
                follow_redirects=True
            )
            response = self.client.post(
                '/admin/user/new/',
                 data=dict(
                    first_name="volu", last_name="vol",
                    email="vol@gmail.com", password="pianovol",
                    roles=[Role(name="volunteer", description="can update location")],
                        ), follow_redirects=True)
            self.assertEqual(response.status_code, 200)


    # Ensure id is correct for the current/logged in user
    def test_get_by_id(self):
        with self.client:
            self.client.post('/admin/login/', data=dict(
                email="admin@gmail.com", password='pianoadmin'
            ), follow_redirects=True)
            self.assertTrue(current_user.id == 1)
            self.assertFalse(current_user.id == 20)


class PianoTests(BaseTestCase):
    # Ensure a logged in superuser can add a new piano
    def test_superuser_can_create_piano(self):
        with self.client:
            self.client.post(
                '/admin/login/',
                data=dict(email="admin@gmail", password="pianoadmin"),
                follow_redirects=True
            )
            response = self.client.post(
                '/admin/piano/new/',
                data=dict(title="test-piano@pdx", lon=123.456, lat=-456.23),
                follow_redirects=True
            )
            self.assertEqual(response.status_code, 200)


        # Ensure a logged in volunteer can update a piano
    def test_volunteer_can_update_piano(self):
        with self.client:
            self.client.post(
                '/admin/login/',
                data=dict(email="vol@gmail.com", password="pianovol"),
                follow_redirects=True
            )
            response = self.client.post(
                '/admin/piano/edit/',
                data=dict(lon=-123.456, lat=456.23, active=1),
                follow_redirects=True
            )
            self.assertEqual(response.status_code, 200)




if __name__ == '__main__':
    unittest.main()
