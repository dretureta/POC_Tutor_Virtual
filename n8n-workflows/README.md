# Workflows de n8n

Este directorio contiene las exportaciones en formato JSON de los workflows de n8n utilizados en el proyecto. Estos archivos pueden ser importados directamente en una instancia de n8n.

## Workflows Disponibles

### 1. `analisis-riesgo.json`

- **Propósito**: Realizar un análisis periódico para identificar a los estudiantes en riesgo.
- **Disparador (Trigger)**: Se ejecuta cada 6 horas (configurable).
- **Lógica**:
    1. Llama al endpoint `/api/students/at-risk` del backend para obtener la lista de estudiantes en riesgo.
    2. Itera sobre cada estudiante.
    3. Crea un mensaje de alerta personalizado.
    4. Envía la alerta al backend a través del endpoint `/api/alerts`.
- **Manejo de Errores**: Si el workflow no puede conectarse al backend, creará una alerta de sistema para notificar el problema.

### 2. `tutor-matematicas.json`

- **Propósito**: Actuar como un agente de IA especializado en tutoría de Matemáticas.
- **Disparador (Trigger)**: Webhook en la ruta `/tutor-math`.
- **Lógica**:
    1. Recibe el `student_id` y el `message` del usuario.
    2. Consulta el perfil del estudiante para obtener su nombre.
    3. Consulta el historial de la conversación.
    4. **Paso de Anonimización**: Un Nodo de Código reemplaza el nombre del estudiante con `[ESTUDIANTE]` en toda la conversación.
    5. Construye un prompt para OpenAI con el historial anonimizado.
    6. Envía la consulta a la API de OpenAI.
    7. **Paso de De-anonimización**: Un Nodo de Código restaura el nombre del estudiante en la respuesta de la IA.
    8. Guarda la conversación original (no anonimizada) en la base de datos.
    9. Devuelve la respuesta final al usuario.
- **Manejo de Errores**: Si la API de OpenAI o la del backend fallan, el workflow responde con un mensaje de error amigable para el usuario.

### 3. `tutor-lengua.json`

- **Propósito**: Actuar como un agente de IA especializado en tutoría de Lengua y Literatura.
- **Disparador (Trigger)**: Webhook en la ruta `/tutor-language`.
- **Lógica**: Idéntica al tutor de matemáticas (incluyendo el proceso de anonimización), pero utiliza un prompt de sistema diferente, enfocado en el análisis de texto, la gramática y la escritura.
- **Manejo de Errores**: Similar al tutor de matemáticas.

---

Para importar estos workflows, ve a tu instancia de n8n, haz clic en "Import from File" y selecciona el archivo JSON deseado. Recuerda configurar las credenciales (PostgreSQL, OpenAI) en n8n para que los nodos funcionen correctamente.
