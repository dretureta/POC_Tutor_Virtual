# Manual de Usuario - Tutor Virtual Ceibal

## 1. Introducción

Bienvenido al sistema de Tutor Virtual Ceibal. Esta guía está diseñada para educadores y administradores y explica cómo utilizar la interfaz para monitorear el progreso de los estudiantes y interactuar con el sistema.

## 2. Roles de Usuario

El sistema cuenta con diferentes roles de usuario para controlar el acceso a las distintas funcionalidades. Principalmente:
- **Profesor (Teacher)**: Este es el rol estándar. Puede ver a los estudiantes, sus detalles, y chatear con los tutores.
- **Administrador (Admin)**: Tiene todos los permisos de un profesor, y además puede realizar acciones a nivel de sistema, como crear nuevos usuarios, ver todas las alertas del sistema, e **importar estudiantes masivamente**.

## 3. Acceso al Sistema

Para acceder al sistema, abre tu navegador web y dirígete a la URL proporcionada (`http://localhost:3000`). Se te pedirá que inicies sesión con tu email y contraseña.

## 3. Dashboard Principal

Al ingresar, la primera pantalla que verás es el **Dashboard Principal**. Esta pantalla te ofrece una vista general del estado de los estudiantes.

### Componentes del Dashboard:

- **Tarjetas de Métricas**: En la parte superior, encontrarás tarjetas que resumen la información clave:
    - **Total Estudiantes**: El número total de estudiantes en el sistema.
    - **En Riesgo**: El número total de estudiantes cuyo rendimiento ha sido marcado como "medio" o "alto" riesgo.
- **Gráfico de Tendencias**: Un gráfico que muestra la evolución del número de estudiantes en riesgo a lo largo del tiempo. Esto te permite identificar patrones y la efectividad de las intervenciones.
- **Lista de Estudiantes**: El área principal del dashboard, donde se muestra una lista de todos los estudiantes. Cada estudiante tiene una tarjeta con su nombre, liceo y su nivel de riesgo actual indicado por una insignia de color.

### Panel de Administración (Solo para Admins)
Si has iniciado sesión como Administrador, verás una sección adicional en el dashboard.

- **Importar Estudiantes desde CSV**: Esta herramienta te permite añadir múltiples estudiantes al sistema de una sola vez.
    1.  **Prepara tu archivo**: Crea un archivo CSV con las columnas `first_name`, `last_name`, y `school`.
    2.  **Selecciona el archivo**: Haz clic en el botón para seleccionar archivos y elige tu archivo CSV.
    3.  **Sube el archivo**: Haz clic en el botón "Subir". El sistema procesará el archivo en segundo plano. Recibirás un mensaje de confirmación y los estudiantes aparecerán en la lista poco después.

## 4. Vista de Detalle del Estudiante

Puedes obtener más información sobre un estudiante específico haciendo clic en su tarjeta en la lista del dashboard. Esto te llevará a la **Vista de Detalle del Estudiante**.

### Secciones de la Vista de Detalle:

- **Perfil del Estudiante**: Muestra el nombre completo del estudiante, su liceo, su nivel de riesgo y sus **puntos totales**.
- **Logros y Recompensas**: Una sección que muestra todas las **insignias** (badges) que el estudiante ha ganado por su buen rendimiento. Puedes pasar el ratón sobre cada insignia para ver por qué fue otorgada.
- **Historial de Evaluaciones**: Una lista detallada de todas las calificaciones que el estudiante ha recibido.
- **Chat con Tutor**: Una interfaz de chat interactiva donde puedes seleccionar el tutor por materia.

## 5. Interacción con el Tutor Virtual (Chat)

En la vista de detalle del estudiante, encontrarás la interfaz de chat. Esta herramienta te permite (o al estudiante, dependiendo del diseño final) interactuar directamente con el tutor virtual de una materia específica.

### Cómo usar el Chat:

1.  **Seleccionar un Tutor**: Encima de la ventana de chat, verás pestañas para los diferentes tutores disponibles (e.g., "Tutor de Matemáticas", "Tutor de Lengua"). Haz clic en la pestaña del tutor con el que deseas conversar.
2.  **Ver el Historial**: La ventana de chat mostrará la conversación previa con el tutor seleccionado.
3.  **Escribir un Mensaje**: En la parte inferior, hay un campo de texto donde puedes escribir tu pregunta.
4.  **Enviar**: Haz clic en el botón "Enviar".
5.  **Recibir Respuesta**: El tutor de IA especializado en esa materia analizará el mensaje y proporcionará una respuesta.

Esta herramienta está diseñada para ofrecer apoyo académico personalizado y al instante en múltiples áreas del conocimiento.
