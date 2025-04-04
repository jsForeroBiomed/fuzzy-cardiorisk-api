import pandas as pd
import numpy as np
import joblib
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def imprimir_metricas(y_true, y_pred):
    print("\n📊 Métricas en conjunto de prueba (test):")
    print(f"MAE : {mean_absolute_error(y_true, y_pred):.2f}")
    print(f"RMSE: {np.sqrt(mean_squared_error(y_true, y_pred)):.2f}")
    print(f"R2  : {r2_score(y_true, y_pred):.2f}")


def cargar_test(path="data/partitioned_data/test.csv"):
    df = pd.read_csv(path)
    X = df[["presion", "colesterol", "imc", "edad", "actividad", "cigarros"]]
    y = df["riesgo_fuzzy"]
    return X, y


if __name__ == "__main__":
    modelo = joblib.load("modelo_tree_tuneado.pkl")
    X_test, y_test = cargar_test()
    pred = modelo.predict(X_test)
    imprimir_metricas(y_test, pred)

