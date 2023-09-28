# test_user_views.py

import os
from unittest import TestCase

from models import db, User, Message, Follows
from app import app, CURR_USER_KEY

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"

db.create_all()

class UserViewTestCase(TestCase):
    """Test views for users."""

# ... (the import statements and other initial setup remain unchanged)

class UserViewTestCase(TestCase):
    """Test views for users."""

    def setUp(self):
        """Create test client, add sample data."""

        db.drop_all()
        db.create_all()

        self.uid = 1111
        u = User(id=self.uid, email="test@test.com", username="testuser", password="testpass")
        db.session.add(u)  # You were missing this line
        db.session.commit()

        self.u = User.query.get(self.uid)
        self.client = app.test_client()

    def tearDown(self):
        res = super().tearDown()
        db.session.rollback()
        return res

    def test_show_user(self):
        """Can we display a user's detail page?"""

        with self.client as c:
            # If needed, simulate a login by setting CURR_USER_KEY in session
            # with c.session_transaction() as sess:
            #     sess[CURR_USER_KEY] = self.uid

            resp = c.get(f"/users/{self.uid}")

            self.assertIn("@testuser", str(resp.data))
            # Expand upon this by checking more data about the user.

    # ... (the rest of the code remains unchanged)
