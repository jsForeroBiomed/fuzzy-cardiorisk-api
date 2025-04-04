import numpy as np
import pandas as pd
from fuzzy_model import predecir


def generar_dataset():
    X, y = [], []
    for presion in range(90, 181, 10):
        for colesterol in range(150, 251, 20):
            for imc in range(18, 36, 3):
                for edad in range(25, 81, 10):
                    for actividad in range(0, 16, 5):
                        for cigarros in [0, 5, 20, 40]:
                            entrada = [presion, colesterol, imc, edad, actividad, cigarros]
                            salida = predecir(*entrada)
                            if isinstance(salida, (float, int)):
                                X.append(entrada)
                                y.append(salida)
    columnas = ["presion", "colesterol", "imc", "edad", "actividad", "cigarros"]
    df = pd.DataFrame(X, columns=columnas)
    df["riesgo_fuzzy"] = y
    return df


if __name__ == "__main__":
    df = generar_dataset()
    df.to_csv("dataset_fuzzy.csv", index=False)
    print(f"{len(df)} registros generados y guardados en 'dataset_fuzzy.csv'")

