from run import app


class TestApplication:
    flask_app = None

    def __init__(self):
        """
        Instance of flask app that will be used for testing.
        """
        self.flask_app = app


test_application = TestApplication()
