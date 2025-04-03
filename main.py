from fastapi import FastAPI
from pydantic import BaseModel
from fuzzy_model import predecir
from database import get_connection

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
    conn = get_connection()
    if conn:
        conn.close()
        return {"status": "success", "message": "Connected to the database successfully."}
    return {"status": "error", "message": "Database connection failed."}


@app.post("/predict")
def predict(data: DatosEntrada) -> dict:
    resultado = predecir(
        data.presion_sistolica,
        data.colesterol_total,
        data.indice_masa_corporal,
        data.edad,
        data.actividad_fisica,
        data.cigarrillos_por_dia
    )
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

