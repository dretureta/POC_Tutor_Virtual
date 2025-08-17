# Guía de Solución de Problemas (Troubleshooting)

Esta guía contiene una lista de problemas comunes que pueden surgir durante la configuración o el uso del sistema y sus posibles soluciones.

---

### Problema 1: Los contenedores de Docker no se inician.

- **Síntoma**: El comando `docker compose up` falla con un error.
- **Causa Común 1**: El Docker Daemon no está corriendo.
    - **Solución**: Asegúrate de que Docker Desktop o el servicio de Docker esté iniciado en tu sistema.
- **Causa Común 2**: Un puerto requerido (3000, 8000, 5432, 5678) ya está en uso por otra aplicación.
    - **Solución**: Detén la aplicación que está usando el puerto o cambia el puerto en el archivo `docker-compose.yml`. Por ejemplo, cambia `"3000:3000"` a `"3001:3000"` para exponer el frontend en el puerto 3001 del host.
- **Causa Común 3**: Permisos de Docker.
    - **Solución**: En Linux, es posible que necesites ejecutar los comandos de Docker con `sudo` o agregar tu usuario al grupo `docker`. Consulta la documentación de Docker para tu sistema operativo.

---

### Problema 2: El frontend no puede conectarse a la API del backend.

- **Síntoma**: La página del dashboard muestra un mensaje de error al intentar cargar los estudiantes.
- **Causa Común 1**: El contenedor del backend (`backend_ceibal`) no está corriendo o está en un estado de error.
    - **Solución**: Ejecuta `docker compose ps` para verificar el estado del contenedor. Si está caído, revisa sus logs con `docker compose logs backend_ceibal` para identificar el error.
- **Causa Común 2**: La URL de la API está mal configurada en el frontend.
    - **Solución**: Verifica la variable `API_BASE_URL` en el archivo `.env` del frontend (si se ha configurado) o el `runtimeConfig` en `nuxt.config.ts`. Por defecto, debería ser `http://localhost:8000/api`.
- **Causa Común 3**: Problemas de CORS.
    - **Solución**: Asegúrate de que la URL desde la que accedes al frontend esté en la lista de `origins` permitidos en el archivo `backend/app/main.py`.

---

### Problema 3: El backend no puede conectarse a la base de datos PostgreSQL.

- **Síntoma**: Los logs del contenedor del backend muestran errores de conexión a la base de datos.
- **Causa Común 1**: El contenedor de `postgres` no se ha iniciado correctamente.
    - **Solución**: Revisa los logs de `postgres` con `docker compose logs postgres_ceibal`.
- **Causa Común 2**: Las credenciales de la base de datos son incorrectas.
    - **Solución**: Asegúrate de que las variables `POSTGRES_USER`, `POSTGRES_PASSWORD`, y `POSTGRES_DB` en el archivo `.env` coincidan con las que espera el backend.

---

### Problema 4: Las migraciones de Alembic fallan.

- **Síntoma**: El contenedor del backend se detiene y los logs muestran un error de Alembic.
- **Causa Común 1**: Hay un error de sintaxis en un archivo de migración.
    - **Solución**: Revisa el último archivo de migración creado en `backend/alembic/versions/` para corregir el error.
- **Causa Común 2**: La base de datos ya contiene tablas que entran en conflicto con la migración.
    - **Solución**: Si estás en un entorno de desarrollo, la solución más sencilla es destruir los volúmenes de Docker (`docker compose down -v`) y empezar con una base de datos limpia. **¡NO HAGAS ESTO EN PRODUCCIÓN!**

---

### Problema 5: n8n no puede conectarse a la API o a la base de datos.

- **Síntoma**: Los workflows de n8n fallan al ejecutar nodos de HTTP Request o al intentar leer de la base de datos.
- **Causa Común 1**: El nombre del host es incorrecto.
    - **Solución**: Dentro de la red de Docker Compose, los servicios se comunican usando el nombre del servicio como hostname. Asegúrate de que en los nodos de n8n, la URL para acceder al backend sea `http://backend:8000` y no `http://localhost:8000`.
- **Causa Común 2**: Las credenciales de la base de datos para n8n son incorrectas.
    - **Solución**: Revisa las variables de entorno `DB_POSTGRESDB_*` en la configuración del servicio `n8n` en `docker-compose.yml`.
