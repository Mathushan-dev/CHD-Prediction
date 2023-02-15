from application.prediction import predict_rfc, prediction_preprocessing


def test_predict_rfc():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is requested (GET)
    THEN check that the response is valid
    :return: None
    """

    X_train, y_train = prediction_preprocessing()
    X_new_dict = {"age": 21, "sex": 1, "height": 170, "weight": 60, "prevalent_stroke": 0, "sys_bp": 120,
                    "dia_bp": 80, "glucose": 80, "tot_chol": 150, "cigs_per_day": 0, "prevalent_hyp": 0,
                    "bp_meds": 0, "diabetes": 0, "education": 2, "current_smoker": 0, "heart_rate": 65}
    X_new = [[int(X_new_dict['sex']), int(X_new_dict['age']), int(X_new_dict['education']),
              int(X_new_dict['current_smoker']),
              int(X_new_dict['cigs_per_day']), int(X_new_dict['bp_meds']), int(X_new_dict['prevalent_stroke']),
              int(X_new_dict['prevalent_hyp']), int(X_new_dict['diabetes']), int(X_new_dict['tot_chol']),
              int(X_new_dict['sys_bp']),
              int(X_new_dict['dia_bp']), round(X_new_dict['weight'] / ((float(X_new_dict['height'])/100.0) ** 2)),
              int(X_new_dict['heart_rate']), int(X_new_dict['glucose'])]]
    prediction_result = predict_rfc(X_train, y_train, X_new)
    assert prediction_result == 1 or prediction_result == 0
