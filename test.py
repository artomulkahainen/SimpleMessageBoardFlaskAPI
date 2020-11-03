import unittest
from app import flask_app
import ast


class RootTest(unittest.TestCase):
    def setUp(self):
        flask_app.config["TESTING"] = True
        flask_app.config["DEBUG"] = False
        self.app = flask_app.test_client()

    def tearDown(self):
        # update soon
        pass

    def test_root(self):
        response = self.app.get("/api/posts", follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_wrong_path_leads_to_404(self):
        response = self.app.get("/api/posts/j", follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    def test_when_postcount_4_return_count_4(self):
        response = self.app.get("/api/posts", follow_redirects=True)
        mydata = ast.literal_eval(response.data.decode("UTF-8"))
        self.assertEqual(4, int(repr(mydata["count"])))

    def test_second_post_is_DUUDIDUUDAADEI(self):
        response = self.app.get("/api/posts", follow_redirects=True)
        mydata = ast.literal_eval(response.data.decode("UTF-8"))
        post_found = False
        for post in mydata["posts"]:
            if post["id"] == 2 and post["post"] == "DUUDIDUUDAADEI":
                post_found = True
        self.assertTrue(post_found)


if __name__ == "__main__":
    unittest.main()