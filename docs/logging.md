# Guía del Sistema de Logging

## 1. Estrategia de Logging

El backend de este proyecto utiliza un sistema de **logging estructurado**. Esto significa que todos los logs se emiten en un formato JSON estándar, en lugar de texto plano.

Las ventajas de este enfoque son:
- **Facilidad de Búsqueda y Filtrado**: Los logs en JSON pueden ser fácilmente ingeridos, parseados y filtrados por plataformas de gestión de logs (como Datadog, Sentry, o el stack ELK).
- **Consistencia**: Todos los logs, ya sean de la aplicación, de errores o de acceso HTTP, siguen el mismo formato.
- **Riqueza de Contexto**: Es fácil añadir campos adicionales y contextuales a los logs (e.g., `user_id`, `request_id`).

## 2. Herramienta Utilizada: `loguru`

Hemos implementado este sistema utilizando la librería [Loguru](https://loguru.readthedocs.io/en/stable/index.html).

La configuración se encuentra en `backend/app/logging_config.py` y se inicializa en `backend/app/main.py`. La configuración actual realiza lo siguiente:
- **Intercepta los logs del sistema `logging` estándar de Python**: Esto asegura que las librerías de terceros que usan el logging estándar (como `uvicorn`) también emitan logs en nuestro formato JSON.
- **Serializa la salida a JSON**: El parámetro `serialize=True` en la configuración del "sink" de loguru se encarga de la conversión a JSON.
- **Envía todos los logs a `stdout`**: Esta es una mejor práctica para aplicaciones en contenedores, ya que permite que el orquestador de contenedores (Docker) gestione la recolección y el enrutamiento de los logs.

## 3. Formato del Log

Un ejemplo de un log de una solicitud HTTP se vería así en la salida del contenedor del backend:

```json
{
    "text": "Request: GET /api/students - Completed in 0.0123s with status 200\\n",
    "record": {
        "elapsed": {
            "repr": "0:00:00.567890",
            "seconds": 0.56789
        },
        "exception": null,
        "extra": {},
        "file": {
            "name": "main.py",
            "path": "/app/app/main.py"
        },
        "function": "log_requests",
        "level": {
            "icon": "ℹ️",
            "name": "INFO",
            "no": 20
        },
        "line": 26,
        "message": "Request: GET /api/students - Completed in 0.0123s with status 200",
        "module": "main",
        "name": "app.main",
        "process": {
            "id": 1,
            "name": "MainProcess"
        },
        "thread": {
            "id": 1401234567890,
            "name": "MainThread"
        },
        "time": {
            "repr": "2024-05-21 10:00:00.123456+00:00",
            "timestamp": 1716285600.123456
        }
    }
}
```

## 4. Cómo Añadir Nuevos Logs

Para añadir logging en cualquier parte del código del backend:

1.  **Importa el logger**:
    ```python
    from loguru import logger
    ```

2.  **Usa los métodos del logger**: Llama al método del nivel de log apropiado (`debug`, `info`, `warning`, `error`, `critical`).
    ```python
    # Ejemplo de log informativo
    logger.info(f"Se ha iniciado el análisis de riesgo para {num_students} estudiantes.")

    # Ejemplo de log de advertencia
    logger.warning(f"Intento de login fallido para el usuario: {email}")

    # Ejemplo de log de error con detalles de una excepción
    try:
        # ... algo que puede fallar ...
    except Exception as e:
        logger.exception("Ha ocurrido un error inesperado al procesar la solicitud.")
    ```

El logger configurado se encargará automáticamente de formatear el mensaje en JSON con todo el contexto relevante.
