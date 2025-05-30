from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import sys
import  os
from src.api.database import get_connection


app = FastAPI()


class DatosEntrada(BaseModel):
    presion_sistolica: float
    colesterol_total: float
    indice_masa_corporal: float
    edad: float
    actividad_fisica: float
    cigarrillos_por_dia: float


@app.get("/check-db")
def check_db():
    try:
        conn = get_connection()
        if conn:
            conn.close()
            return {"status": "success", "message": "Connected to the database successfully."}
    except Exception as e:
        return {"status": "error", "message": f"Exception: {str(e)}"}


@app.post("/predict")
def predict(data: DatosEntrada) -> dict:
    entrada = np.array([[

        data.presion_sistolica,
        data.colesterol_total,
        data.indice_masa_corporal,
        data.edad,
        data.actividad_fisica,
        data.cigarrillos_por_dia

        ]])

    modelo = joblib.load("modelo_tree_tuneado.pkl")
    resultado = modelo.predict(entrada)[0]
    
    conn = get_connection()
    cursor = conn.cursor()


    query = """
        INSERT INTO predicciones (
            presion_sistolica,
            colesterol_total,
            indice_masa_corporal,
            edad,
            actividad_fisica,
            cigarrillos_por_dia,
            riesgo
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        data.presion_sistolica,
        data.colesterol_total,
        data.indice_masa_corporal,
        data.edad,
        data.actividad_fisica,
        data.cigarrillos_por_dia,
        resultado
    )

    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()

    return {
        "input": data.dict(),
        "riesgo_cardiovascular": resultado
        }
