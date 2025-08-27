# Guía de Privacidad y Protección de Datos

## 1. Compromiso con la Privacidad

La protección de la privacidad de los estudiantes es una prioridad máxima para el proyecto del Tutor Virtual Ceibal. Este documento describe las medidas técnicas implementadas para asegurar que la Información Personal Identificable (PII) de los estudiantes sea manejada de forma segura y no sea expuesta a servicios de terceros innecesariamente.

## 2. Proceso de Anonimización de Datos

El componente principal que interactúa con un servicio externo es el workflow de tutoría, que envía datos a la API de OpenAI. Para prevenir la fuga de PII, hemos implementado un proceso de anonimización y de-anonimización directamente en los workflows de n8n.

### Flujo del Proceso:

1.  **Obtención de Datos**: Cuando un estudiante envía un mensaje al tutor, el workflow se inicia y obtiene dos piezas de información clave:
    -   El perfil del estudiante (específicamente, su nombre y apellido).
    -   El historial de la conversación.

2.  **Nodo de Anonimización**: Antes de enviar cualquier dato a OpenAI, el workflow pasa la conversación por un **Nodo de Código** que ejecuta un script de anonimización. Este script:
    -   Toma el nombre y apellido del estudiante.
    -   Busca y reemplaza todas las apariciones de ese nombre en todo el historial de la conversación con un marcador genérico: `[ESTUDIANTE]`.
    -   Esto se aplica tanto al historial previo como al nuevo mensaje enviado por el usuario.

3.  **Llamada a OpenAI**: La API de OpenAI recibe únicamente la versión anonimizada de la conversación. No tiene acceso al nombre real del estudiante ni a otros datos de su perfil. El prompt de sistema que se envía a OpenAI también le indica que use el marcador `[ESTUDIANTE]` para referirse al usuario.

4.  **Nodo de De-anonimización**: Una vez que OpenAI devuelve una respuesta, esta puede contener el marcador (ej. "¡Claro, [ESTUDIANTE]!"). Para que la conversación se sienta natural, la respuesta pasa por un segundo **Nodo de Código**. Este script:
    -   Busca y reemplaza el marcador `[ESTUDIANTE]` con el nombre real del estudiante.

5.  **Guardado y Respuesta**:
    -   La respuesta, ya con el nombre real restaurado, es lo que se le muestra al usuario en el frontend.
    -   En la base de datos, se guarda la conversación completa y **no anonimizada**, para que el historial que ve el usuario sea coherente y natural.

### Resumen del Flujo:

```
                  +--------------------------------+
                  |       Workflow de n8n          |
                  |                                |
[Usuario] -> [Chat] -> [Backend] -> | Webhook -> Obtener Datos -> Anonimizar -> OpenAI -> De-anonimizar -> Guardar -> Responder | -> [Usuario]
                  |                                |
                  +--------------------------------+
                                     |
                                     V
                           +-------------------+
                           |   API de OpenAI   |
                           | (Solo ve datos    |
                           |   anonimizados)   |
                           +-------------------+
```

## 3. Conclusión

Gracias a este proceso, podemos aprovechar el poder de los modelos de lenguaje avanzados mientras nos aseguramos de que los datos personales de los estudiantes nunca salgan de nuestro entorno controlado. Esto garantiza un entorno de aprendizaje seguro y privado.
