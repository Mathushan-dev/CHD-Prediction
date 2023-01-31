from tests.test_application import test_application


def test_index():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    :return: None
    """
    with test_application.flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b'Start monitoring your risk of developing Coronary Heart Disease' in response.data
        assert b'CHD Prediction' in response.data
