# Guía de Accesibilidad (a11y)

## 1. Introducción

La accesibilidad (a menudo abreviada como a11y) es una parte fundamental de este proyecto. Nuestro objetivo es asegurar que la aplicación del Tutor Virtual Ceibal sea usable por la mayor cantidad de personas posible, incluyendo aquellas con discapacidades visuales, motoras o de otro tipo.

Este documento establece las pautas y mejores prácticas a seguir durante el desarrollo para mantener y mejorar la accesibilidad de la aplicación.

## 2. Pautas Generales

### 2.1. HTML Semántico

- **Usa los elementos HTML correctos para su propósito**. Utiliza `<nav>`, `<main>`, `<header>`, `<aside>`, `<button>`, etc., en lugar de depender exclusivamente de `<div>` y `<span>`. Esto proporciona una estructura clara que los lectores de pantalla pueden interpretar.
- **Encabezados**: Usa los encabezados (`<h1>` a `<h6>`) para estructurar el contenido de forma lógica y jerárquica. No saltes niveles de encabezado.

### 2.2. Navegación por Teclado

- **Todo debe ser operable por teclado**: Cualquier acción que se pueda realizar con un ratón debe poder realizarse también con un teclado.
- **Foco visible**: Asegúrate de que los elementos interactivos (enlaces, botones, campos de formulario) tengan un indicador de foco claro y visible. No elimines el `outline` por defecto sin proporcionar una alternativa.
- **Orden lógico**: El orden en que se navega con la tecla `Tab` debe seguir el flujo visual de la página.

### 2.3. Contraste de Color

- **Contraste suficiente**: El texto y los elementos importantes de la interfaz deben tener un ratio de contraste de color suficiente con su fondo para ser legibles. Utiliza herramientas de comprobación de contraste para verificar que cumples con las pautas de la WCAG (mínimo 4.5:1 para texto normal).
- **No confíes solo en el color**: No uses el color como la única forma de transmitir información. Por ejemplo, para indicar un error, además de usar el color rojo, incluye un ícono y un texto descriptivo.

## 3. Pautas Específicas para Componentes

### 3.1. Formularios

- **Etiquetas (`<label>`)**: Cada campo de formulario (`<input>`, `<textarea>`, `<select>`) debe tener una etiqueta `<label>` asociada explícitamente mediante el atributo `for`. Si una etiqueta visible no es apropiada, usa una clase `sr-only` (screen-reader only) o un `aria-label`.
- **Mensajes de Error**: Los errores de validación deben ser claros, descriptivos y estar asociados programáticamente con el campo correspondiente usando `aria-describedby`.

### 3.2. Enlaces y Botones

- **Texto descriptivo**: El texto de un enlace o el `aria-label` de un botón debe describir claramente lo que sucederá al activarlo. Evita textos ambiguos como "Haz clic aquí" o "Ver más".
- **Diferencia entre enlace y botón**: Usa un enlace (`<a>`) para navegar a una nueva página o recurso. Usa un botón (`<button>`) para realizar una acción en la página actual (e.g., enviar un formulario, abrir un modal).

### 3.3. Contenido Dinámico (Chats, Alertas)

- **Regiones Vivas (ARIA Live Regions)**: Para el contenido que se actualiza dinámicamente, como nuevos mensajes en un chat o notificaciones, utiliza el atributo `aria-live` en el contenedor.
    - `aria-live="polite"`: Anunciará los cambios cuando el usuario termine su tarea actual. Es la opción más común.
    - `aria-live="assertive"`: Interrumpirá al usuario para anunciar un cambio importante. Úsalo con moderación.

## 4. Herramientas Recomendadas

- **Lighthouse (en Chrome DevTools)**: Proporciona una auditoría automática de accesibilidad que puede detectar muchos problemas comunes.
- **Extensiones de navegador**: Herramientas como "axe DevTools" o "WAVE" pueden ayudar a identificar problemas de accesibilidad directamente en la página.
- **Lectores de pantalla**: Familiarízate con cómo usar un lector de pantalla como NVDA (Windows), VoiceOver (macOS) o TalkBack (Android) para probar la experiencia de usuario no visual.
