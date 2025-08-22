# Arquitectura del Sistema - POC Tutor Virtual Ceibal

## 1. Resumen

Este documento describe la arquitectura del sistema para la Prueba de Concepto (POC) del Tutor Virtual Ceibal. El sistema está diseñado con una arquitectura de microservicios orquestada a través de Docker Compose, lo que permite una clara separación de responsabilidades y escalabilidad futura.

El stack tecnológico principal incluye:
- **Backend**: FastAPI (Python)
- **Base de Datos**: PostgreSQL
- **Orquestador de Workflows**: n8n
- **Frontend**: Vue.js 3 con Nuxt (a ser desarrollado)
- **Contenedorización**: Docker

## 2. Diagrama de Arquitectura

(Diagrama a ser añadido - representaría los 4 servicios principales comunicándose entre sí)

```
+----------------+      +----------------+      +----------------+
|   Frontend     | <--> |   Backend      | <--> |   PostgreSQL   |
| (Nuxt, Vue.js) |      |   (FastAPI)    |      |   (DB)         |
+----------------+      +-------+--------+      +----------------+
                                |
                                v
+----------------+      +----------------+
|   Usuario      | <--> |      n8n       |
| (Navegador)    |      | (Workflows)    |
+----------------+      +----------------+
```

## 3. Componentes Principales

### 3.1. Backend (Servicio `backend`)

- **Framework**: FastAPI sobre Python. Ofrece un alto rendimiento y generación automática de documentación de API (Swagger UI y ReDoc).
- **Responsabilidades**:
    - Exponer una API RESTful para gestionar estudiantes, evaluaciones, y conversaciones.
    - Conectar con la base de datos PostgreSQL para la persistencia de datos.
    - Implementar la lógica de negocio, como el análisis de riesgo de los estudiantes.
    - Servir como punto de entrada para las solicitudes del frontend y los workflows de n8n.
- **Estructura**:
    - `main.py`: Punto de entrada de la aplicación FastAPI.
    - `api/`: Módulos de enrutadores de la API (e.g., `students.py`, `evaluations.py`).
    - `crud/`: Funciones para la interacción con la base de datos (Crear, Leer, Actualizar, Borrar).
    - `models/`: Modelos de datos de SQLAlchemy que definen el esquema de la base de datos.
    - `schemas/`: Esquemas de Pydantic para la validación y serialización de datos de la API.
    - `services/`: Lógica de negocio desacoplada (e.g., `risk_analysis.py`).
    - `database.py`: Configuración de la conexión a la base de datos.

### 3.2. Base de Datos (Servicio `postgres`)

- **Sistema**: PostgreSQL. Una base de datos relacional robusta y de código abierto.
- **Responsabilidades**:
    - Almacenar todos los datos persistentes de la aplicación, incluyendo:
        - `students`: Información de los estudiantes.
        - `subjects`: Materias del currículo.
        - `evaluations`: Calificaciones y evaluaciones de los estudiantes.
        - `conversations`: Historial de chats con los tutores.
- **Migraciones**: Se gestionan a través de `Alembic` para controlar las versiones del esquema de la base de datos de manera programática.

### 3.3. Orquestador de Workflows (Servicio `n8n`)

- **Herramienta**: n8n. Una herramienta de automatización de workflows de código abierto.
- **Responsabilidades**:
    - Orquestar tareas complejas que involucran múltiples pasos y servicios.
    - **Análisis de Riesgo Periódico**: Un workflow que se ejecuta cada cierto tiempo, consulta la API del backend para obtener datos de estudiantes, y ejecuta análisis para detectar a aquellos en riesgo.
    - **Agentes Tutores**: Workflows que se activan mediante webhooks, reciben el contexto de una conversación, interactúan con la API de OpenAI para generar una respuesta de tutoría, y guardan el historial de la conversación.

### 3.4. Frontend (Servicio `frontend`)

- **Framework**: Nuxt (sobre Vue.js 3). Un framework moderno para construir aplicaciones universales de Vue.js.
- **Responsabilidades**:
    - Proporcionar la interfaz de usuario para los administradores y/o educadores.
    - **Dashboard**: Visualizar estadísticas, listas de estudiantes y niveles de riesgo.
    - **Vista de Estudiante**: Mostrar el perfil detallado de un estudiante, su historial académico y conversaciones.
    - **Interfaz de Chat**: Permitir la interacción en tiempo real con los agentes tutores (a través de la API del backend y los workflows de n8n).

## 4. Flujo de Datos

1.  **Generación de Datos**: Un script (`mock-data/generate_students.py`) genera datos simulados y los guarda en formato JSON. Estos datos pueden ser cargados en la base de datos a través de la API o un script de importación.
2.  **Visualización de Datos**: El `Frontend` solicita datos a la `API del Backend` para mostrar información en los dashboards.
3.  **Análisis de Riesgo (n8n)**: El servicio `n8n` periódicamente llama al endpoint `/api/students` del `Backend`, procesa los datos, y podría actualizar el nivel de riesgo de un estudiante a través de otro endpoint.
4.  **Interacción del Tutor (Chat en Tiempo Real con WebSockets)**:
    1.  El `Frontend` inicia una conexión WebSocket con el `Backend` al abrir la interfaz de chat.
    2.  El usuario envía un mensaje a través del WebSocket.
    3.  El `Backend` recibe el mensaje y actúa como un "puente", llamando al webhook HTTP correspondiente en `n8n` (ej. `/tutor-math`).
    4.  El workflow de `n8n` se ejecuta de forma síncrona: consulta a OpenAI y realiza las acciones necesarias. La respuesta del tutor se devuelve como la respuesta a la llamada HTTP del webhook.
    5.  El `Backend` recibe la respuesta de n8n y la envía de vuelta al `Frontend` a través de la conexión WebSocket.
    6.  El `Frontend` recibe el mensaje en tiempo real y lo muestra en la interfaz de chat.

## 5. Despliegue

- **Orquestación**: `docker-compose.yml` define y configura todos los servicios, redes y volúmenes.
- **Variables de Entorno**: Un archivo `.env` se utiliza para gestionar las configuraciones sensibles (como claves de API y credenciales de base de datos) de forma segura.
