# Documentación de la API

Esta documentación describe los endpoints disponibles en la API del backend del Tutor Virtual Ceibal.

Para una documentación interactiva y completa, una vez que el servicio del backend esté corriendo, puedes acceder a:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Endpoints de Estudiantes (`/api/students`)

### `GET /api/students/`

- **Descripción**: Obtiene una lista de todos los estudiantes.
- **Parámetros de Query**:
    - `skip` (opcional, `int`): Número de registros a saltar. Default: `0`.
    - `limit` (opcional, `int`): Número máximo de registros a devolver. Default: `100`.
- **Respuesta Exitosa (`200 OK`)**: Un array de objetos `Student`.
    ```json
    [
      {
        "first_name": "Juan",
        "last_name": "Perez",
        "school": "IAVA",
        "id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
        "risk_level": "low",
        "evaluations": []
      }
    ]
    ```

### `POST /api/students/`

- **Descripción**: Crea un nuevo estudiante.
- **Cuerpo de la Solicitud**: Un objeto `StudentCreate`.
    ```json
    {
      "first_name": "Maria",
      "last_name": "Gomez",
      "school": "Liceo 5"
    }
    ```
- **Respuesta Exitosa (`200 OK`)**: El objeto del estudiante recién creado.

### `GET /api/students/{student_id}`

- **Descripción**: Obtiene los detalles de un estudiante específico por su ID.
- **Parámetros de Ruta**:
    - `student_id` (requerido, `uuid`): El ID del estudiante.
- **Respuesta Exitosa (`200 OK`)**: Un objeto `Student`.
- **Respuesta de Error (`404 Not Found`)**: Si el estudiante no se encuentra.

### `GET /api/students/at-risk/`

- **Descripción**: Obtiene una lista de estudiantes que han sido identificados con un nivel de riesgo "medio" o "alto" por el servicio de análisis de riesgo.
- **Respuesta Exitosa (`200 OK`)**: Un array de objetos `Student`.

## Endpoints de Evaluaciones (`/api/evaluations`)

### `POST /api/evaluations/`

- **Descripción**: Registra una nueva evaluación para un estudiante en una materia específica.
- **Cuerpo de la Solicitud**: Un objeto `EvaluationCreate`.
    ```json
    {
      "score": 8,
      "subject_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
      "student_id": "b2c3d4e5-f6a7-8901-2345-67890abcdef1"
    }
    ```
- **Respuesta Exitosa (`200 OK`)**: El objeto de la evaluación recién creada.

## Endpoints de Materias (`/api/subjects`)

### `GET /api/subjects/{subject_name}/analytics`

- **Descripción**: Obtiene estadísticas básicas para una materia específica, identificada por su nombre.
- **Parámetros de Ruta**:
    - `subject_name` (requerido, `string`): El nombre de la materia (e.g., "Matemáticas").
- **Respuesta Exitosa (`200 OK`)**: Un objeto con las analíticas.
    ```json
    {
      "subject_id": "c3d4e5f6-a7b8-9012-3456-7890abcdef12",
      "subject_name": "Matemáticas",
      "evaluation_count": 150,
      "average_score": 7.53
    }
    ```
- **Respuesta de Error (`404 Not Found`)**: Si la materia no se encuentra.

## Endpoint de Salud (`/health`)

### `GET /health`

- **Descripción**: Un endpoint simple para verificar que el servicio está activo y respondiendo.
- **Respuesta Exitosa (`200 OK`)**:
    ```json
    {
      "status": "ok"
    }
    ```
