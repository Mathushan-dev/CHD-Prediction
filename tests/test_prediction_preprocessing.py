from application.prediction import prediction_preprocessing


def test_prediction_preprocessing():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is requested (GET)
    THEN check that the response is valid
    :return: None
    """

    assert prediction_preprocessing()[0] is not None
    assert prediction_preprocessing()[1] is not None
