# Guía de Instalación Detallada - POC Tutor Virtual Ceibal

## 1. Introducción

Bienvenido a la guía de instalación completa para la Prueba de Concepto (POC) del Tutor Virtual Ceibal. Este documento te guiará a través de todos los pasos necesarios para clonar, configurar y ejecutar el proyecto completo en tu máquina local utilizando Docker.

La arquitectura del proyecto se basa en microservicios orquestados por Docker Compose, incluyendo un backend en FastAPI, un frontend en Nuxt.js, una base de datos PostgreSQL y una instancia de n8n para la automatización de workflows.

## 2. Prerrequisitos

Antes de comenzar, asegúrate de tener instalado el siguiente software en tu sistema.

| Herramienta      | Propósito                                  | Link de Instalación                                                              |
| ---------------- | ------------------------------------------ | -------------------------------------------------------------------------------- |
| **Git**          | Para clonar el código fuente del proyecto. | [git-scm.com/downloads](https://git-scm.com/downloads)                             |
| **Docker Desktop** | Para construir y ejecutar los contenedores. | [docker.com/products/docker-desktop](https://docker.com/products/docker-desktop) |

Docker Desktop incluye **Docker Compose**, que es esencial para este proyecto. Verifica tu instalación ejecutando `docker --version` y `docker compose version` en tu terminal.

## 3. Pasos de Instalación

### Paso 1: Obtener el Código Fuente

Primero, clona el repositorio del proyecto en una carpeta de tu elección en tu máquina local.

```bash
# Reemplaza <URL_DEL_REPOSITORIO> con la URL real del repositorio Git
git clone <URL_DEL_REPOSITORIO>

# Navega al directorio del proyecto
cd poc-tutor-virtual
```

### Paso 2: Configuración de Variables de Entorno

La configuración de la aplicación se gestiona a través de variables de entorno. Necesitarás crear un archivo `.env` a partir del ejemplo proporcionado.

1.  **Copia el archivo de ejemplo**:
    ```bash
    cp .env.example .env
    ```
2.  **Edita el archivo `.env`**: Abre el archivo `.env` con un editor de texto. Deberás configurar las siguientes variables:

    -   `OPENAI_API_KEY`: **(Requerido)**. Aquí debes pegar tu clave secreta de la API de OpenAI. El sistema no funcionará sin ella.
    -   `SECRET_KEY`: Clave secreta utilizada para firmar los tokens de autenticación JWT. El valor por defecto es seguro para desarrollo, pero deberías cambiarlo para producción.
    -   Otras variables como las de la base de datos y n8n ya vienen preconfiguradas para el entorno de Docker y generalmente no necesitan ser modificadas para el desarrollo local.

### Paso 3: Construir y Ejecutar los Contenedores

Este es el paso principal. El siguiente comando le dirá a Docker Compose que construya las imágenes personalizadas para el backend y el frontend, y que inicie todos los servicios definidos en `docker-compose.yml`.

```bash
# Ejecuta este comando desde la raíz del proyecto
docker compose up -d --build
```

-   `--build`: Fuerza la reconstrucción de las imágenes. Es útil la primera vez o si has hecho cambios en el código fuente o en los `Dockerfile`.
-   `-d`: (Modo "detached") Ejecuta los contenedores en segundo plano, para que no ocupen tu terminal.

Este proceso puede tardar varios minutos la primera vez, ya que Docker descargará las imágenes base y construirá los proyectos.

### Paso 4: Verificación y Configuración Inicial

Una vez que el comando anterior termine, verifica que todos los servicios estén corriendo correctamente.

1.  **Verifica los contenedores**:
    ```bash
    docker compose ps
    ```
    Deberías ver 4 servicios (`postgres_ceibal`, `n8n_ceibal`, `backend_ceibal`, `frontend_ceibal`) con el estado `running` o `up`.

2.  **Crea tu primer usuario (Admin)**:
    -   Abre tu navegador y ve a la documentación de la API: **`http://localhost:8000/docs`**.
    -   Busca el endpoint `POST /api/auth/users/`.
    -   Haz clic en "Try it out".
    -   En el cuerpo de la solicitud, introduce un email y una contraseña. **Importante**: para crear el primer usuario administrador, cambia el `role` a `"admin"`.
    -   Haz clic en "Execute".

3.  **Inicia sesión en el Frontend**:
    -   Ve a la aplicación frontend: **`http://localhost:3000/login`**.
    -   Usa el email y la contraseña que acabas de crear para iniciar sesión.

¡Felicidades! El entorno está completamente configurado y funcionando.

## 4. Flujo de Trabajo para Desarrollo Diario

-   **Ver logs**: Para ver la salida de un servicio específico (muy útil para debugging):
    ```bash
    docker compose logs -f backend_ceibal
    # O para el frontend:
    docker compose logs -f frontend_ceibal
    ```
-   **Detener el entorno**:
    ```bash
    docker compose down
    ```
-   **Detener y eliminar volúmenes** (¡Esto borrará tu base de datos!):
    ```bash
    docker compose down -v
    ```
-   **Ejecutar pruebas del backend**:
    ```bash
    docker compose exec backend pytest
    ```

## 5. Solución de Problemas Comunes

-   **Error de "port is already allocated"**: Significa que un puerto (3000, 8000, 5678, 5432) ya está en uso en tu máquina. Detén el programa que lo usa o cambia el puerto en el archivo `docker-compose.yml`.
-   **El frontend no se conecta a la API**: Asegúrate de que el contenedor `backend_ceibal` esté corriendo. Revisa sus logs para ver si hay errores.
-   **Errores al construir las imágenes**: Asegúrate de tener una conexión a internet estable y suficiente espacio en disco. Si un build falla, intenta ejecutar `docker compose build --no-cache` para forzar una reconstrución limpia.
