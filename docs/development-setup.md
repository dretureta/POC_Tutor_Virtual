# Guía de Configuración del Entorno de Desarrollo

Este documento proporciona las instrucciones para configurar y ejecutar el proyecto del Tutor Virtual Ceibal en un entorno de desarrollo local.

## 1. Prerrequisitos

Asegúrate de tener instaladas las siguientes herramientas en tu sistema:
- **Docker**: [Instrucciones de instalación](https://docs.docker.com/get-docker/)
- **Docker Compose**: Generalmente se incluye con Docker Desktop. [Instrucciones](https://docs.docker.com/compose/install/)
- **Git**: Para clonar el repositorio.

## 2. Pasos de Configuración

### Paso 1: Clonar el Repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd poc-tutor-virtual
```

### Paso 2: Configurar las Variables de Entorno

El proyecto utiliza un archivo `.env` para gestionar las variables de entorno. Se proporciona un archivo de ejemplo `.env.example`.

1.  Crea una copia de `.env.example` y renómbrala a `.env`:
    ```bash
    cp .env.example .env
    ```

2.  Abre el archivo `.env` y edita las variables según sea necesario. Como mínimo, deberás proporcionar tu propia `OPENAI_API_KEY`.

    ```env
    OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
    DATABASE_URL=postgresql://postgres:postgres@postgres:5432/tutor_poc
    N8N_BASIC_AUTH_ACTIVE=true
    N8N_BASIC_AUTH_USER=admin
    N8N_BASIC_AUTH_PASSWORD=admin123
    ENVIRONMENT=development
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    POSTGRES_DB=tutor_poc
    ```

### Paso 3: Construir y Levantar los Contenedores

Una vez que el archivo `.env` está configurado, puedes levantar todos los servicios usando Docker Compose.

```bash
docker compose up -d --build
```

- `-d`: Ejecuta los contenedores en modo "detached" (en segundo plano).
- `--build`: Fuerza la reconstrucción de las imágenes de Docker si ha habido cambios en los `Dockerfile` o en el código fuente.

Este comando hará lo siguiente:
- Descargará las imágenes de `postgres` y `n8n`.
- Construirá las imágenes para los servicios `backend` y `frontend`.
- Creará e iniciará los cuatro contenedores.
- Creará la red `ceibal-net` para que los servicios se comuniquen entre sí.
- Creará los volúmenes `postgres_data` y `n8n_data` para la persistencia de datos.

### Paso 4: Verificar que los Servicios estén Corriendo

Puedes verificar el estado de los contenedores con:

```bash
docker compose ps
```

Deberías ver los cuatro servicios (`postgres_ceibal`, `n8n_ceibal`, `backend_ceibal`, `frontend_ceibal`) en estado `running` o `up`.

## 3. Acceso a los Servicios

Una vez que todo está corriendo, puedes acceder a los diferentes componentes del sistema:

- **Backend (API)**: `http://localhost:8000`
- **Documentación de la API (Swagger)**: `http://localhost:8000/docs`
- **Frontend**: `http://localhost:3000`
- **n8n**: `http://localhost:5678` (Credenciales: `admin` / `admin123` según el `.env`)
- **Base de Datos (PostgreSQL)**: Accesible en el puerto `5432` desde el host.

## 4. Gestión de la Base de Datos

### Migraciones

El backend utiliza Alembic para gestionar las migraciones de la base de datos. Al iniciar, el contenedor del backend ejecuta automáticamente las migraciones pendientes (`alembic upgrade head`).

Para crear una nueva migración después de realizar cambios en los modelos de `SQLAlchemy` (en `backend/app/models/`), puedes ejecutar:

```bash
docker compose exec backend alembic revision --autogenerate -m "Descripción de la migración"
```

Asegúrate de revisar el archivo de migración generado en `backend/alembic/versions/` antes de aplicarlo.

## 5. Ejecución de Pruebas

Las pruebas para el backend están escritas con `pytest`. Para ejecutarlas, utiliza el siguiente comando, que las corre dentro del contenedor del backend donde todas las dependencias están instaladas:

```bash
docker compose exec backend pytest
```

## 6. Detener el Entorno

Para detener todos los servicios, ejecuta:

```bash
docker compose down
```

Si además quieres eliminar los volúmenes (¡esto borrará los datos de tu base de datos y de n8n!), ejecuta:

```bash
docker compose down -v
```
