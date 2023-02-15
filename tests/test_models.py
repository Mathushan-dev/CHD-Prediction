from application.models import Users


def test_Users():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is requested (GET)
    THEN check that the response is valid
    :return: None
    """

    X_new_dict = {"age": 21, "sex": 1, "height": 170, "weight": 60, "prevalent_stroke": 0, "sys_bp": 120,
                  "dia_bp": 80, "glucose": 80, "tot_chol": 150, "cigs_per_day": 0, "prevalent_hyp": 0,
                  "bp_meds": 0, "diabetes": 0, "education": 2, "current_smoker": 0, "heart_rate": 65}

    user_to_create = Users(username="test_debug",
                           email_address="test_debug@test_debug.com",
                           password="test_debug_password",
                           age=21, sex=1, height=170, weight=60,
                           prevalent_stroke=0, sys_bp=120, dia_bp=80,
                           glucose=80, tot_chol=150, cigs_per_day=0,
                           prevalent_hyp=0, bp_meds=0, diabetes=0,
                           education=2, current_smoker=0, heart_rate=65)
    assert user_to_create.username == "test_debug"
    assert user_to_create.email_address == "test_debug@test_debug.com"
    assert user_to_create.age == 21
    assert user_to_create.sex == 1
    assert user_to_create.height == 170
    assert user_to_create.weight == 60
    assert user_to_create.prevalent_stroke == 0
    assert user_to_create.sys_bp == 120
    assert user_to_create.dia_bp == 80
    assert user_to_create.glucose == 80
    assert user_to_create.tot_chol == 150
    assert user_to_create.cigs_per_day == 0
    assert user_to_create.prevalent_hyp == 0
    assert user_to_create.bp_meds == 0
    assert user_to_create.diabetes == 0
    assert user_to_create.education == 2
    assert user_to_create.current_smoker == 0
    assert user_to_create.heart_rate == 65

