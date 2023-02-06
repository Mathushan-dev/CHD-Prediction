from application.routes import extract_from_form


def test_extract_from_form():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is requested (GET)
    THEN check that the response is valid
    :return: None
    """

    assert extract_from_form(None, True, True)["height"] is not None
    assert extract_from_form(None, True, True)["weight"] is not None
    assert extract_from_form(None, True, True)["sys_bp"] is not None
    assert extract_from_form(None, True, True)["dia_bp"] is not None
    assert extract_from_form(None, True, True)["glucose"] is not None
    assert extract_from_form(None, True, True)["heart_rate"] is not None
