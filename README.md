# Task Manager API
Mini API para gestionar reservas, desarrollada como proyecto base del curso de Metodologías de Desarrollo para la actividad autónoma.
## Objetivo del proyecto
Construir una aplicación pequeña que permita practicar flujo de trabajo moderno con Python, Git, GitHub
## Funcionalidades iniciales
- Listar reservas.
- Crear reserva.
- Marcar reservas como completadas.
## Tecnologías utilizadas
- Python
- FastAPI
- Uvicorn
- Git
- GitHub
## Estructura del proyecto
```text
task-api/
├── app/
│ ├── main.py
│ ├── config.py
│ ├── data/
│ ├── models/
│ ├── routes/
│ ├── services/
│ └── utils/
├── docs/
├── test/
├── README.md
└── requirements.txt
```
Ejecución local
1. Crear entorno virtual:
python -m venv venv
2. Activar entorno virtual:
venv\Scripts\Activate.ps1
3. Instalar dependencias:
pip install -r requirements.txt
4. Ejecutar la API:
uvicorn app.main:app --reload
5. Abrir documentación:
http://127.0.0.1:8000/docs
Estado del proyecto
Versión inicial del proyecto.

##Equipo de trabajo
Anthony Alejandro Minga Campoverde

## Convención de commits
El equipo utilizará mensajes de commit con el siguiente formato:
- feat: nueva funcionalidad
- fix: corrección de errores
- docs: cambios en documentación
- refactor: mejora interna del código
- test: pruebas
- chore: tareas de configuración

## Proyecto en capas
La estructura modular se encuentra ahora consolidada en la carpeta `app/`.