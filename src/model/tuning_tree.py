import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error
import joblib


def cargar_datos():
    train = pd.read_csv("data/partitioned_data/train.csv")
    val = pd.read_csv("data/partitioned_data/val.csv")
    return pd.concat([train, val], axis=0)


def dividir_xy(df):
    X = df[["presion", "colesterol", "imc", "edad", "actividad", "cigarros"]]
    y = df["riesgo_fuzzy"]
    return X, y


def imprimir_metricas(y_true, y_pred):
    print(f"MAE : {mean_absolute_error(y_true, y_pred):.2f}")
    print(f"RMSE: {np.sqrt(mean_squared_error(y_true, y_pred)):.2f}")
    print(f"R2  : {r2_score(y_true, y_pred):.2f}")


if __name__ == "__main__":
    df = cargar_datos()
    X, y = dividir_xy(df)

    param_grid = {
        "max_depth": [3, 5, 6, 7, 8],
        "min_samples_split": [2, 5, 10],
        "min_samples_leaf": [1, 2, 4],
        "ccp_alpha": [0.0, 0.001, 0.01]
    }

    modelo = DecisionTreeRegressor(random_state=42)
    grid_search = GridSearchCV(modelo, param_grid, cv=5, scoring="neg_mean_absolute_error", n_jobs=-1)
    grid_search.fit(X, y)

    print("🎯 Mejores hiperparámetros encontrados:")
    print(grid_search.best_params_)

    print("\n📊 Métricas en validación cruzada (mejor modelo):")
    best_model = grid_search.best_estimator_
    preds = best_model.predict(X)
    imprimir_metricas(y, preds)

    joblib.dump(best_model, "modelo_tree_tuneado.pkl")
    print("\n✅ Modelo tuneado guardado como 'modelo_tree_tuneado.pkl'")
