# test_user_views.py
"""User view tests."""

import os
from unittest import TestCase
from models import db, User, Message

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"

from app import app, CURR_USER_KEY

db.create_all()
app.config['WTF_CSRF_ENABLED'] = False

class UserViewTestCase(TestCase):
    """Test views for users."""

    def setUp(self):
        """Create test client and add sample data."""

        User.query.delete()
        Message.query.delete()

        self.client = app.test_client()

        self.testuser = User.signup(username="testuser",
                                    email="test@test.com",
                                    password="testuser",
                                    image_url=None)
        db.session.commit()

    def test_show_user(self):
        """Can we show a user's profile page?"""

        with self.client as c:
            resp = c.get(f"/users/{self.testuser.id}")
            self.assertIn("@testuser", str(resp.data))

    def test_signup_user(self):
        """Can we sign a user up?"""

        with self.client as c:
            resp = c.post("/signup", data={
                "username": "newuser",
                "password": "password",
                "email": "new@test.com",
                "image_url": ""
            })

            # Check if we get a redirect after a successful signup
            self.assertEqual(resp.status_code, 302)
            
            user = User.query.filter(User.username == "newuser").first()
            self.assertIsNotNone(user)
