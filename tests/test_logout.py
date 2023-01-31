from tests.test_application import test_application


def test_logout():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/logout' page is requested (GET)
    THEN check that the response is valid
    :return: None
    """
    with test_application.flask_app.test_client() as test_client:
        response = test_client.post('/logout')
        assert response.status_code == 200
        assert b'Start monitoring your risk of developing Coronary Heart Disease' in response.data
        assert b'View Health Data' in response.data
