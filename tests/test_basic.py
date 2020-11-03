import os
import unittest

from app import app
from models.models import db


class BasicTest(unittest.TestCase):
    # executed prior to each test
    def setUp(self):
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        app.config["DEBUG"] = False
        self.app = app.test_client()

        self.assertEqual(app.debug, False)

    # executed after each test
    def tearDown(self):
        pass

    """def test_main_page(self):
        response = self.app.get("/api/posts", follow_redirects=True)
        print(response)
        self.assertEqual(response.status_code, 200)"""


if __name__ == "__main__":
    unittest.main()
