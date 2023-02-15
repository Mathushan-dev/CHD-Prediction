import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from imblearn.over_sampling import SMOTE


def prediction_preprocessing():
    df = pd.read_csv("https://raw.githubusercontent.com/theleadio/datascience_demo/master/framingham.csv")
    df.nunique()
    df.dropna(axis=0, inplace=True)

    sm = SMOTE(sampling_strategy='minority')
    oversampled_X, oversampled_Y = sm.fit_resample(df.drop('TenYearCHD', axis=1), df['TenYearCHD'])
    oversampled_df = pd.concat([pd.DataFrame(oversampled_Y), pd.DataFrame(oversampled_X)], axis=1)

    X = oversampled_df.drop(columns=['TenYearCHD'])
    y = oversampled_df['TenYearCHD']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    return X_train, y_train


def predict_fitbit(X_new_dict):
    X_new = [[X_new_dict['sex'], X_new_dict['age'], X_new_dict['education'],
             X_new_dict['current_smoker'],
              X_new_dict['cigs_per_day'], X_new_dict['bp_meds'], X_new_dict['prevalent_stroke'],
              X_new_dict['prevalent_hyp'], int(X_new_dict['diabetes']), X_new_dict['tot_chol'],
              X_new_dict['sys_bp'],
              X_new_dict['dia_bp'], round(X_new_dict['weight'] / ((float(X_new_dict['height'])/100.0) ** 2)),
              X_new_dict['heart_rate'], X_new_dict['glucose']]]
    X_train, y_train = prediction_preprocessing()
    # knn_prediction = predict_knn(X_train, y_train, X_new)
    # mlp_prediction = predict_mlp(X_train, y_train, X_new)
    rfc_prediction = predict_rfc(X_train, y_train, X_new)
    # gbc_prediction = predict_gbc(X_train, y_train, X_new)
    return rfc_prediction


def predict(X_new_dict):
    X_new = [[int(X_new_dict['sex']), int(X_new_dict['age']), int(X_new_dict['education']),
              int(X_new_dict['current_smoker']),
              int(X_new_dict['cigs_per_day']), int(X_new_dict['bp_meds']), int(X_new_dict['prevalent_stroke']),
              int(X_new_dict['prevalent_hyp']), int(X_new_dict['diabetes']), int(X_new_dict['tot_chol']),
              int(X_new_dict['sys_bp']),
              int(X_new_dict['dia_bp']), round(X_new_dict['weight'] / ((float(X_new_dict['height'])/100.0) ** 2)),
              int(X_new_dict['heart_rate']), int(X_new_dict['glucose'])]]
    X_train, y_train = prediction_preprocessing()
    # knn_prediction = predict_knn(X_train, y_train, X_new)
    # mlp_prediction = predict_mlp(X_train, y_train, X_new)
    rfc_prediction = predict_rfc(X_train, y_train, X_new)
    # gbc_prediction = predict_gbc(X_train, y_train, X_new)
    return rfc_prediction


def predict_knn(X_train, y_train, X_new):
    knn_model = KNeighborsClassifier(n_neighbors=2)
    knn_model.fit(X_train, y_train)
    y_new = knn_model.predict(X_new)
    return y_new


def predict_mlp(X_train, y_train, X_new):
    mlp_model = MLPClassifier()
    mlp_model.fit(X_train, y_train)
    y_new = mlp_model.predict(X_new)
    return y_new


def predict_rfc(X_train, y_train, X_new):
    rfc_model = RandomForestClassifier()
    rfc_model.fit(X_train, y_train)
    y_new = rfc_model.predict(X_new)
    return y_new


def predict_gbc(X_train, y_train, X_new):
    gbc_model = GradientBoostingClassifier()
    gbc_model.fit(X_train, y_train)
    y_new = gbc_model.predict(X_new)
    return y_new
