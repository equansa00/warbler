# test_message_model.py
"""Message model tests."""

import os
from unittest import TestCase
from models import db, User, Message

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"

from app import app

db.create_all()

class MessageModelTestCase(TestCase):
    """Test model for messages."""

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

    def test_message_create(self):
        """Does basic model work for Message?"""

        m = Message(
            text="This is a test message",
            user_id=self.testuser.id
        )

        db.session.add(m)
        db.session.commit()

        # Check if the message was created and if it's linked to the user
        self.assertEqual(len(self.testuser.messages), 1)
        self.assertEqual(self.testuser.messages[0].text, "This is a test message")
