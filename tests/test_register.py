from tests.test_application import test_application


def test_register():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/register' page is requested (GET)
    THEN check that the response is valid
    :return: None
    """
    with test_application.flask_app.test_client() as test_client:
        response = test_client.post('/register')
        assert response.status_code == 200
        assert b'Please Create your Account' in response.data
        assert b'Already have an account?' in response.data
