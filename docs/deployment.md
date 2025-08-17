# Guía de Despliegue

Este documento contiene notas y consideraciones para desplegar el proyecto en un entorno de producción.

*(Esta sección se detallará más a fondo en la Fase 4 del proyecto.)*

## Consideraciones para Producción

### 1. Variables de Entorno

- **Seguridad**: El archivo `.env` no debe ser incluido en el control de versiones. En un entorno de producción, las variables de entorno deben ser gestionadas de forma segura a través del proveedor de hosting o una herramienta de gestión de secretos.
- **Modo Debug**: La variable `ENVIRONMENT` debe ser cambiada a `production`. Esto debería deshabilitar los modos de debug en FastAPI y Nuxt.

### 2. Base de Datos

- **Backups**: Configurar backups automáticos y periódicos para la base de datos PostgreSQL.
- **Contraseñas**: Utilizar contraseñas seguras y robustas para el usuario de la base de datos.

### 3. Seguridad

- **HTTPS**: Configurar un reverse proxy (como Nginx o Traefik) para gestionar el tráfico entrante y habilitar SSL/TLS para que toda la comunicación sea a través de HTTPS.
- **CORS**: Ajustar la configuración de CORS en el backend para permitir únicamente el dominio del frontend de producción.

### 4. Rendimiento

- **Workers de Gunicorn**: En lugar de `uvicorn --reload`, el `command` del servicio `backend` debería ser reemplazado por un servidor WSGI de producción como Gunicorn, con múltiples workers.
  ```
  gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app -b 0.0.0.0:8000
  ```
- **Build de Producción del Frontend**: El `command` del servicio `frontend` debe cambiar de `npm run dev` a `npm run build` y luego `npm run start` para servir los archivos estáticos optimizados.

### 5. Monitoreo

- **Health Checks**: Implementar health checks más robustos en Docker Compose para asegurar que los contenedores se reinicien si no están saludables.
- **Logging**: Configurar un sistema de logging centralizado para agregar los logs de todos los servicios.
