# Guía de Rendimiento del Frontend

## 1. Estrategia de Rendimiento

El rendimiento es un aspecto clave de la experiencia de usuario. Una aplicación rápida y fluida es más agradable de usar. Nuestra estrategia de rendimiento se centra en dos áreas principales:
1.  **Reducir el tiempo de carga inicial**: Asegurarnos de que el usuario vea el contenido interactivo lo más rápido posible.
2.  **Mantener un tamaño de paquete (bundle) saludable**: Evitar que la aplicación se vuelva demasiado pesada a medida que añadimos nuevas funcionalidades y dependencias.

## 2. Técnicas de Optimización Implementadas

### Carga Perezosa (Lazy Loading) de Componentes

Hemos implementado la carga perezosa para los componentes que son "pesados" (contienen mucha lógica o librerías grandes) o que no son críticos para el renderizado inicial de la página.

En Nuxt 3, esto se logra de forma muy sencilla prefijando el nombre del componente con la palabra `Lazy`.

**Componentes Afectados:**
-   `<LazyRiskTrendChart />`: El componente de gráficos, que incluye la librería `chart.js`, ahora solo se carga cuando es necesario, en lugar de bloquear la carga inicial del dashboard.
-   `<LazyChatInterface />`: La interfaz de chat, que también es un componente complejo, se carga de forma perezosa en la página de detalle del estudiante.

Esta técnica mejora significativamente el "Time to Interactive" (TTI) de las páginas más importantes.

## 3. Análisis del Paquete (Bundle Analysis)

Para ayudarnos a entender qué contribuye al tamaño final de nuestra aplicación, hemos integrado una herramienta de visualización de paquetes.

### Cómo Usarla

1.  Abre una terminal en el directorio `frontend/`.
2.  Ejecuta el siguiente comando:
    ```bash
    ANALYZE=true npm run build
    ```
3.  Una vez que el proceso de build termine, se abrirá automáticamente una nueva pestaña en tu navegador con un mapa interactivo. También se guardará un archivo `bundle-stats.html` en la raíz del proyecto.

### Cómo Interpretar el Informe

El mapa visual muestra cada una de las dependencias de nuestro proyecto y cuánto espacio ocupan en el paquete final. Esto nos permite:
-   Identificar librerías "pesadas" que podríamos reemplazar por alternativas más ligeras.
-   Detectar si estamos importando código que no usamos (tree-shaking ineficiente).
-   Tomar decisiones informadas antes de añadir una nueva dependencia, evaluando su impacto en el tamaño total de la aplicación.

Se recomienda ejecutar este análisis periódicamente para mantener el control sobre el rendimiento de la aplicación a medida que evoluciona.
