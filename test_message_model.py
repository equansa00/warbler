import os
from unittest import TestCase
from sqlalchemy import exc

from models import db, User, Message, Follows
from app import app

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"

db.create_all()

class MessageModelTestCase(TestCase):
    """Test functionality of the Message model."""

    def setUp(self):
        """Set up test client and sample data."""
        db.drop_all()
        db.create_all()

        self.user = User(id=1111, username="testuser", email="test@test.com", password="password")
        db.session.add(self.user)
        db.session.commit()

    def tearDown(self):
        res = super().tearDown()
        db.session.rollback()
        return res

    def test_message_create(self):
        """Does creating a message work?"""
        msg = Message(id=2222, text="hello", user_id=self.user.id)
        db.session.add(msg)
        db.session.commit()

        # Add more tests: 
        # 1. Check if message requires a user_id.
        # 2. Check if message has timestamp by default.
        # 3. Any additional functionality in Message model you want to test.
