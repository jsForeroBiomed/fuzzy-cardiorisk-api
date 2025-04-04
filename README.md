# 🫀 API de Predicción de Riesgo Cardiovascular (versión ML optimizada)

Este proyecto implementa una API REST construida con **FastAPI** que predice el **riesgo cardiovascular** de un paciente utilizando un modelo de **árbol de decisión** entrenado a partir de reglas borrosas de tipo Mamdani.  
Las predicciones se almacenan automáticamente en una base de datos **MySQL**.

> El sistema original basado en lógica borrosa fue usado para generar un dataset sintético, que luego se utilizó para entrenar un modelo de Machine Learning más escalable para entornos de producción.


## 🚀 Tecnologías utilizadas

- Python 3.11  
- FastAPI  
- Scikit-learn  
- Uvicorn  
- NumPy  
- Pandas  
- Matplotlib  
- NetworkX  
- Scikit-Fuzzy  
- MySQL Connector  
- Python Dotenv

## 📦 Instalación

### 1. Clonar el repositorio

```
git clone https://github.com/jsForeroBiomed/fuzzy-cardiorisk-api.git
cd fuzzy-cardiorisk-api
```

### 2. Crear y activar el entorno Conda

```
conda create -n fuzzy-api-py311 python=3.11
conda activate fuzzy-api-py311
```

### 3. Instalar las dependencias

```
pip install -r requirements.txt
```

### 4. Crear un archivo `.env` con tus credenciales de base de datos

```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=tu_contraseña
DB_NAME=cardiorisk_api
```

---

## 🧪 Ejecución local

```
python -m uvicorn main:app --reload
```

Accede a la documentación interactiva:  
🔗 [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📤 Endpoints

### 🔍 `GET /check-db`

Verifica la conexión con la base de datos.

---

### 🔮 `POST /predict`

Recibe los siguientes campos en JSON:

```
{
  "presion_sistolica": 130,
  "colesterol_total": 220,
  "indice_masa_corporal": 27,
  "edad": 55,
  "actividad_fisica": 3,
  "cigarrillos_por_dia": 10
}
```

Y retorna:

```
{
  "input": { ... },
  "riesgo_cardiovascular": 42.75
}
```

Además, la predicción queda registrada automáticamente en la base de datos MySQL para análisis posterior.

---

## 🧠 Sobre el modelo

Este proyecto utiliza un modelo de **árbol de decisión** (`DecisionTreeRegressor`) entrenado con un dataset generado artificialmente a partir de un sistema experto borroso de tipo Mamdani.

- El modelo mantiene alta interpretabilidad.  
- Fue optimizado con validación cruzada (`GridSearchCV`) sobre `train + val`.  
- La evaluación final se realizó sobre un `test.csv` independiente, con un MAE de 0.04 y R² de 1.00, demostrando que el modelo de ML replica el sistema experto borroso, pero haciéndolo mejor optimizado y más escalable en producción. 

---

## 🗃️ Estructura de la tabla `predicciones`

La base de datos fue creada en **MySQL**, y la tabla `predicciones` tiene la siguiente estructura:

```
CREATE TABLE predicciones (
    id INT NOT NULL AUTO_INCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    presion_sistolica FLOAT DEFAULT NULL,
    colesterol_total FLOAT DEFAULT NULL,
    indice_masa_corporal FLOAT DEFAULT NULL,
    edad FLOAT DEFAULT NULL,
    actividad_fisica FLOAT DEFAULT NULL,
    cigarrillos_por_dia FLOAT DEFAULT NULL,
    riesgo FLOAT DEFAULT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;
```

---

## 📂 Requisitos del sistema

`requirements.txt` incluye:

```
fastapi==0.110.1
uvicorn==0.29.0
numpy==1.26.4
scikit-fuzzy==0.4.2
mysql-connector-python==8.3.0
python-dotenv==1.0.1
networkx==3.3
matplotlib==3.8.4
pandas==2.2.1
scikit-learn==1.4.1.post1
```

Todos compatibles con Python 3.11 ✅

---

## 🔐 Seguridad

Este proyecto utiliza un archivo `.env` para mantener las credenciales fuera del código. Recuerda incluir `.env` en tu `.gitignore`.

```
.env
```

---

## 📄 Licencia

Este proyecto es libre de uso con fines académicos o de investigación.  
Puedes modificarlo para extenderlo, integrarlo con frontend o desplegarlo en la nube.
```

