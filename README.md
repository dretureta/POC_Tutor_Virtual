# POC Tutor Virtual Ceibal

> **Nota del Proyecto:** Este proyecto ha completado su fase de desarrollo inicial. Para un resumen completo del estado final, las funcionalidades implementadas y el roadmap de próximos pasos, por favor consulta el **[Documento de Traspaso (`HANDOVER.md`)](./HANDOVER.md)**.

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

Para obtener una guía de instalación completa y detallada, paso a paso, por favor consulta el siguiente documento:

### ➡️ [**Guía de Instalación Detallada (`INSTALACION.md`)**](./INSTALACION.md)

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
