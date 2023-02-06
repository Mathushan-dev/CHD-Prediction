from application.routes import logout_page
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
        assert response.status_code == 302
        assert b'Redirecting' in response.data
        assert b'/login' in response.data
        response = logout_page(debug=True)
        assert 'Start monitoring your risk of developing Coronary Heart Disease' in response
        assert 'View Health Data' in response
