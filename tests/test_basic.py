import unittest
from app import app
import ast


class RootTest(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        self.app = app.test_client()

    def tearDown(self):
        # update soon
        pass

    def test_root(self):
        response = self.app.get("/api/posts", follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_wrong_path_leads_to_404(self):
        response = self.app.get("/api/posts/j", follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    def test_when_postcount_3_return_count_3(self):
        response = self.app.get("/api/posts", follow_redirects=True)
        mydata = ast.literal_eval(response.data.decode("UTF-8"))
        for post in repr(mydata):
            if post["id"] == 3:
                print(post["post"])
        self.assertEqual(3, int(repr(mydata["count"])))

    """def test_id3_post_contains_jea(self):
        response = self.app.get("/api/posts", follow_redirects=True)
        mydata = ast.literal_eval(response.data.decode("UTF-8"))
        for post in repr(mydata):
            if int(post["id"]) == 3:
                print(post["post"])"""


if __name__ == "__main__":
    unittest.main()
