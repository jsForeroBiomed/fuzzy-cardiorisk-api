import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor, export_text
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error
import joblib


def cargar_datos():
    train = pd.read_csv("data/partitioned_data/train.csv")
    val = pd.read_csv("data/partitioned_data/val.csv")
    return train, val


def dividir_xy(df):
    X = df[["presion", "colesterol", "imc", "edad", "actividad", "cigarros"]]
    y = df["riesgo_fuzzy"]
    return X, y


def imprimir_metricas(y_true, y_pred, nombre=""):
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)

    print(f"\n📊 Métricas {nombre}")
    print(f"MAE : {mae:.2f}")
    print(f"RMSE: {rmse:.2f}")
    print(f"R2  : {r2:.2f}")


def entrenar_y_validar(X_train, y_train, X_val, y_val):
    modelo = DecisionTreeRegressor(max_depth=6, random_state=42)
    modelo.fit(X_train, y_train)
    pred_train = modelo.predict(X_train)
    pred_val = modelo.predict(X_val)

    imprimir_metricas(y_train, pred_train, "Train")
    imprimir_metricas(y_val, pred_val, "Validación")

    return modelo


def mostrar_reglas(modelo, columnas):
    reglas = export_text(modelo, feature_names=columnas)
    print("\nÁrbol de decisión:")
    print(reglas)


def guardar_modelo(modelo, archivo="modelo_baseline_tree.pkl"):
    joblib.dump(modelo, archivo)
    print(f"\nModelo guardado en: {archivo}")


if __name__ == "__main__":
    train, val = cargar_datos()
    X_train, y_train = dividir_xy(train)
    X_val, y_val = dividir_xy(val)

    modelo = entrenar_y_validar(X_train, y_train, X_val, y_val)
    mostrar_reglas(modelo, X_train.columns.tolist())
    guardar_modelo(modelo)

