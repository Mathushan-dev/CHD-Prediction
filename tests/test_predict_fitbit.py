from application.prediction import predict_fitbit


def test_predict_fitbit():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is requested (GET)
    THEN check that the response is valid
    :return: None
    """

    prediction_result = predict_fitbit({"age": 21, "sex": 1, "height": 170, "weight": 60, "prevalent_stroke": 0, "sys_bp": 120,
                                        "dia_bp": 80, "glucose": 80, "tot_chol": 150, "cigs_per_day": 0, "prevalent_hyp": 0,
                                        "bp_meds": 0, "diabetes": 0, "education": 2, "current_smoker": 0, "heart_rate": 65})
    assert prediction_result == 1 or prediction_result == 0
