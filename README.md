# 🫀 API de Predicción de Riesgo Cardiovascular con Lógica Borrosa

Este proyecto implementa una API REST construida con **FastAPI** que predice el **riesgo cardiovascular** de un paciente utilizando un modelo borroso tipo **Mamdani**. Las predicciones se almacenan en una base de datos **MySQL**.


## 🚀 Tecnologías utilizadas

- Python 3.11  
- FastAPI  
- Scikit-Fuzzy  
- Uvicorn  
- MySQL  
- Pydantic  
- Dotenv


## 📦 Instalación

### 1. Clonar el repositorio

```
git clone https://github.com/tu-usuario/fuzzy-cardiorisk-api.git
cd fuzzy-cardiorisk-api
```

### 2. Crear y activar un entorno virtual

```
conda create -n fuzzy-cardiorisk-api python=3.11
conda activate fuzzy-cardiorisk-api
```

### 3. Instalar las dependencias

```
pip install -r requirements.txt
```

### 4. Crear un archivo `.env` con tus credenciales de base de datos

```dotenv
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=tu_contraseña
DB_NAME=cardiorisk_api
```

---

## 🧪 Ejecución local

```
uvicorn main:app --reload
```

Accede a la documentación interactiva:  
🔗 [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📤 Endpoints

### 🔍 `GET /check-db`

Verifica la conexión con la base de datos.

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
  "riesgo_cardiovascular": 50.0
}
```

Además, guarda automáticamente la predicción en la base de datos MySQL.

---

## 🗃️ Estructura de la tabla `predicciones`

```
CREATE TABLE predicciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    presion_sistolica FLOAT,
    colesterol_total FLOAT,
    indice_masa_corporal FLOAT,
    edad FLOAT,
    actividad_fisica FLOAT,
    cigarrillos_por_dia FLOAT,
    riesgo FLOAT
);
```

## 🧠 Modelo borroso Mamdani

El sistema experto usa lógica borrosa con funciones de membresía triangulares y reglas del tipo:

```
Si presión es alta Y colesterol es alto Y edad es mayor, entonces riesgo es alto
```

El modelo está definido en el archivo `fuzzy_model.py`.

---

## ❓¿Por qué lógica borrosa?

Fuzzy Logic permite tomar decisiones con base en **conocimiento experto humano**, sin necesidad de grandes volúmenes de datos. Es ideal en contextos médicos donde se requiere **interpretabilidad**, manejo de **incertidumbre lingüística** y explicaciones basadas en reglas.

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

