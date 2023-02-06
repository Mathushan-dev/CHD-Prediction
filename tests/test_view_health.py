from application.routes import monitor_page, view_health_page
from tests.test_application import test_application


def test_view_health():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/monitor' page is requested (GET)
    THEN check that the response is valid
    :return: None
    """
    with test_application.flask_app.test_client() as test_client:
        response = test_client.post('/view_health')
        assert response.status_code == 302
        assert b'Redirecting' in response.data
        assert b'/login' in response.data
        health_factors = {"age": 21, "sex": 1, "height": 170, "weight": 60, "prevalent_stroke": 0, "sys_bp": 120,
                          "dia_bp": 80, "glucose": 80, "tot_chol": 150, "cigs_per_day": 0, "prevalent_hyp": 0,
                          "bp_meds": 0, "diabetes": 0, "education": 2, "current_smoker": 0, "heart_rate": 65}
        response = view_health_page(debug=True, health=health_factors)
        assert 'View your most recent health data' in response

