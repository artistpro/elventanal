# 📋 Brief de Descubrimiento & Estrategia: Proyecto Digital Signage

Este documento tiene como objetivo **capturar todo tu contexto, ideas, visión y requerimientos** para transformar el prototipo inicial en un sistema de cartelería digital universal, escalable e hiper-interactivo.

Responde o expande sobre los puntos que consideres clave. No hay respuestas incorrectas; entre más contexto me des, más preciso y potente será el diseño arquitectónico y las fases de desarrollo.

---

## 🎯 1. Visión del Producto y Casos de Uso
1. **Entornos de Despliegue**:
   - ¿El sistema se usará principalmente para **Streams en vivo 24/7** (OBS, YouTube, Twitch, Kick)?
   - ¿También planeas usarlo en **pantallas físicas** (locales comerciales, eventos, monitores en oficina)?
2. **Nivel de Automatización**:
   - ¿Quieres que el tablero funcione **100% autónomo** (rotación programada de módulos y fuentes de datos)?
   - ¿O necesitas **intervención/control en tiempo real** (cambiar temas, enviar alertas o imágenes al vuelo desde un panel de control)?

---

## 📡 2. Módulos e Insumos de Información (Data Sources)
¿Qué tipos de datos y contenidos te gustaría que los módulos puedan procesar y mostrar?
- [ ] **Financiero / Crypto**: Precios en tiempo real, gráficos Binance/CoinGecko, Fear & Greed Index, libros de órdenes.
- [ ] **Noticias & Feeds**: Lectura automática de RSS (periódicos, blogs), posts de X/Twitter, alertas de tendencias.
- [ ] **Contenido Multimedia**: Banners promocionales, reproductores de video/audio, conversor de imágenes a Arte ASCII.
- [ ] **Clima & Geografía**: Pronóstico del tiempo local/global, mapas dinámicos.
- [ ] **Interactividad Social & Métricas**: Suscriptores de YouTube en vivo, chat en tiempo real, alertas de donaciones/miembros.
- [ ] **Widgets de Productividad**: Relojes mundiales, temporizadores, frases motivacionales, agendas.
- ¿Hay alguna otra API, fuente de datos o tipo de contenido específico que tengas en mente?

---

## 🎨 3. Estética Visual, Temas y Layouts (UI/UX)
1. **Líneas de Diseño / Temas**:
   - Ya tenemos la estética **Cyberpunk / Matrix Neón** (Crypto Hacker).
   - ¿Qué otros estilos te gustaría incorporar? *(Ejemplos: Minimalista Corporate, TV Newsroom / Noticiero, Retro Synthwave 80s, Dark Glassmorphism, Neumorfismo, Gaming)*.
2. **Disposición de Pantalla (Layout Engine)**:
   - ¿Quieres poder cambiar la distribución en tiempo real? *(Ejemplo: Pantalla completa, 2 columnas, grid de 4 zonas, o barra de marquesina inferior fija + zona principal configurable)*.

---

## 🎛️ 4. Panel de Control y Experiencia del Administrador
1. **Control Remoto**:
   - ¿Cómo sueñas controlar lo que se muestra en pantalla? *(Web Admin responsive desde el celular/laptop, Bot de Telegram/Discord, Extensión de Chrome)*.
2. **Gestión de Pantallas / Multicanal**:
   - ¿Planeas controlar **una sola pantalla/stream a la vez**, o quieres una consola centralizada que maneje **múltiples canales/pantallas independientes** simultáneamente?

---

## 🚀 5. Roadmap Sugerido y Priorización de Etapas
Para avanzar sin saturar y garantizando calidad (aislamiento del riesgo):
- **Etapa 1 (Core & Grid System)**: Arquitectura base modular, layout configurable y migración del módulo Crypto/ASCII.
- **Etapa 2 (Integración de Datos & RSS)**: Módulos de noticias, feeds automáticos, marquesinas y climas.
- **Etapa 3 (Panel Admin & Multitenant)**: Dashboard de control avanzado con Firebase/WebSockets y presets de layouts.
- **Etapa 4 (Automatización & AI)**: Generación o resumen inteligente de noticias con IA para la marquesina.
