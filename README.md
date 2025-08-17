# POC Tutor Virtual Ceibal

## Objetivo

Crear una Prueba de Concepto (POC) funcional de un sistema de tutor virtual que analiza datos de evaluaciones estudiantiles (simulados) y genera agentes tutores adaptativos usando n8n y OpenAI.

## Stack Tecnológico

- **Backend**: FastAPI + PostgreSQL
- **Orquestador**: n8n (workflows visuales)
- **LLM**: OpenAI GPT-4 Turbo
- **Frontend**: Vue.js 3 + Nuxt
- **Despliegue**: Docker Compose
- **Datos**: Mock data realistas del contexto educativo uruguayo

## Estructura del Proyecto

```
poc-tutor-virtual/
├── backend/                 # FastAPI + PostgreSQL
├── frontend/               # Vue.js 3 + Nuxt
├── n8n-workflows/          # Workflows exportados
├── mock-data/              # Datos simulados
├── docs/                   # Documentación técnica
├── docker-compose.yml      # Orquestación completa
├── .env.example            # Variables de entorno
└── README.md               # Documentación
```

## Configuración y Ejecución

A continuación se presentan los pasos para levantar el entorno de desarrollo local. Para una guía más detallada, consulta el documento de [configuración de desarrollo](./docs/development-setup.md).

### 1. Prerrequisitos

- Docker y Docker Compose

### 2. Configuración

1.  **Clonar el repositorio**:
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd poc-tutor-virtual
    ```
2.  **Crear archivo de entorno**: Copia el archivo de ejemplo `.env.example` a `.env` y añade tu clave de API de OpenAI.
    ```bash
    cp .env.example .env
    ```
3.  **Levantar los servicios**:
    ```bash
    docker compose up -d --build
    ```

### 3. Acceso a los Servicios

- **Backend (API)**: `http://localhost:8000`
- **Documentación de la API (Swagger)**: `http://localhost:8000/docs`
- **Frontend**: `http://localhost:3000`
- **Frontend**: `http://localhost:3000` (requiere iniciar sesión)
- **n8n**: `http://localhost:5678`

### Nota sobre Autenticación

La aplicación ahora cuenta con un sistema de autenticación. Después de levantar los servicios, el primer paso es registrar un nuevo usuario. Puedes hacerlo a través de la documentación de la API en `http://localhost:8000/docs` (endpoint `POST /api/auth/users/`). Luego, usa esas credenciales para iniciar sesión en el frontend.

## Pruebas

Para ejecutar las pruebas del backend, utiliza el siguiente comando:

```bash
docker compose exec backend pytest
```
