from tests.test_application import test_application


def test_login():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is requested (GET)
    THEN check that the response is valid
    :return: None
    """
    with test_application.flask_app.test_client() as test_client:
        response = test_client.post('/login')
        assert response.status_code == 200
        assert b'Please Login' in response.data
        assert b'Do not have an account?' in response.data
