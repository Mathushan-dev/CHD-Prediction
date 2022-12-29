CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(30) NOT NULL,
    email_address VARCHAR(50) NOT NULL,
    password_hash VARCHAR(60) NOT NULL,

    #optional
    f_name VARCHAR(30),
    l_name VARCHAR(30),
    dob DATE,
    #0-male, 1-female
    sex SMALLINT,
    weight SMALLINT,
    height SMALLINT,
    sys_bp SMALLINT,
    dia_bp SMALLINT,
    glucose SMALLINT,
    tot_chol SMALLINT,
    cigs_per_day SMALLINT,
    prevalent_hyp SMALLINT,
    bp_meds SMALLINT,
    diabetes SMALLINT,
    education SMALLINT,
    current_smoker SMALLINT,
    heart_rate SMALLINT,
    prevalent_stroke SMALLINT
);
