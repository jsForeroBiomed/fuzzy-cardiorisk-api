import pandas as pd
from sklearn.model_selection import train_test_split


def cargar_dataset(path="data/raw_fuzzy/dataset_fuzzy.csv"):
    return pd.read_csv(path)


def particionar_dataset(df, test_size=0.3, val_size=0.3, random_state=42):
    X = df.drop(columns=["riesgo_fuzzy"])
    y = df["riesgo_fuzzy"]
    
    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=test_size, random_state=random_state)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=val_size, random_state=random_state)

    train = pd.concat([X_train, y_train], axis=1)
    val = pd.concat([X_val, y_val], axis=1)
    test = pd.concat([X_test, y_test], axis=1)

    return train, val, test


def guardar_particiones(train, val, test):
    train.to_csv("data/partitioned_data/train.csv", index=False)
    val.to_csv("data/partitioned_data/val.csv", index=False)
    test.to_csv("data/partitioned_data/test.csv", index=False)


if __name__ == "__main__":
    df = cargar_dataset()
    train, val, test = particionar_dataset(df)
    guardar_particiones(train, val, test)
