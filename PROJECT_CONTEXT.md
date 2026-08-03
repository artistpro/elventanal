# PROJECT_CONTEXT.md — Especificación Maestra & Fotografía General del Proyecto 📺🚀

> **Proyecto:** Digital Signage Engine (Plataforma Universal de Cartelería Digital e Interactiva Multisectorial)  
> **Versión de Documento:** 3.0.0 (Consolidación Integral de Investigaciones de Mercado, Hardware, Módulos y Negocio)  
> **Estado:** Especificación Arquitectónica Completa & Plan de Escalabilidad  
> **Bóveda de Origen:** `Obsidian Vault/Proyectos Artist Pro/Digital Signage`  
> **Sincronización:** Syncthing (Windows Local ⇄ Linux System ⇄ Dispositivos Móviles)

---

## 🧭 1. Declaración de Principios y Alcance Holístico

**Digital Signage Engine** es un **ecosistema universal de cartelería digital, interactiva y multiseectorial**. El desarrollo previo del tablero `crypto-hacker-dashboard` (BCH Monitor System v2) actúa **únicamente como un prototipo o demo técnica de referencia**.

La plataforma no está limitada a ningún nicho ni estética particular: es un **motor modular parametrizable** diseñado para operar tanto en **transmisiones continuas 24/7** (YouTube, Twitch, Kick) como en **redes de pantallas físicas comerciales e institucionales** (hoteles, restaurantes, universidades, centros comerciales, estadios, hospitales y juntas comunitarias).

- **Puntaje de Validación de Negocio**: **78/100 (Pursue)** con potencial de **90-95/100** al integrar capacidades multi-cadena, inteligencia contextual e interactividad hiperlocal.

---

## 🏬 2. Análisis del Mercado de Publicidad Digital (Digital OOH) en Colombia

### A. Diagnóstico de Competidores Actuales en Colombia
Investigaciones de mercado en el entorno colombiano (Bogotá, Medellín, Cali, Eje Cafetero, Barranquilla) identifican tres tipos de actores tradicionales:

1. **Empresas OOH Tradicionales** (*Publiguías, Interavia Publicidad Exterior*):
   - Poseen grandes redes de vallas LED y mupis en vías principales y centros comerciales.
   - **Brecha/Limitación**: Enfoque 100% en venta de espacios publicitarios estáticos o loops de video rígidos. **Cero interactividad, cero integración de datos en tiempo real y cero contenido adaptativo**.
2. **Fabricantes/Integradores de Hardware** (*Valorem Outdoor, Ledtech, integradores Samsung/LG*):
   - Enfocados en la venta e instalación física de pantallas.
   - **Brecha/Limitación**: Carecen de una capa de software/contenido inteligente, dependientes de CMS de terceros rígidos.
3. **Redes Cautivas en Transporte/Retail**:
   - Concesiones en TransMilenio, Metro de Medellín, aeropuertos (Opaín) o centros comerciales.
   - **Brecha/Limitación**: Poco espacio para contenido generado por la comunidad o interactividad con el transeúnte.

### B. Ventaja Competitiva Diferencial de Digital Signage
- **Dinamismo e Interactividad en Tiempo Real**: Datos vivos (APIs/WebSockets) sin necesidad de recargar pantallas.
- **Canal de Interacción vía WhatsApp Business API**: Integración directa con la app de mensajería dominante en Colombia para recibir mensajes, encuestas o registros sin obligar a descargar aplicaciones.
- **Enfoque de Medio Comunitario + Negocio**: Posicionamiento como servicio de información útil para el transeúnte/espectador, lo que reduce la fatiga publicitaria y aumenta el valor percibido por patrocinadores.
- **Curaduría de Contenido impulsada por IA**: Integración con el agente **Hermes** para sintetizar noticias, clasificar alertas y alimentar las marquesinas automáticamente.

---

## 🌐 3. Catálogo Completo de Verticales & Módulos Sectoriales

El sistema cuenta con conectores y plantillas parametrizables para múltiples sectores:

### 1. 📊 Sector Economía, Mercados & Finanzas
- Indicadores macroeconómicos de Colombia (TRM Dólar/Euro, inflación, tasa de interés Banco de la República, petróleo WTI/Brent, café, oro).
- Monitoreo de bolsas bursátiles (BVC, S&P 500, Nasdaq), empresas y criptomonedas (BCH, BTC, ETH, SOL).
- Gráficos de tendencias, libros de órdenes y medidores de volatilidad contextual.

### 2. 🏛️ Sector Política & Actualidad Nacional/Internacional
- Cinta marquesina (Ticker) de titulares noticiosos de última hora vía feeds RSS seleccionados.
- Cobertura especial de debates legislativos, elecciones, proyectos de ley y acuerdos.
- Paneles de información pública, alertas ciudadanas y comunicados de alcaldías/gobernaciones.

### 3. ⚽ Sector Deportes & Fútbol
- Marcadores y resultados en tiempo real (Liga BetPlay Colombia, Champions League, Eliminatorias FIFA, Copa Libertadores).
- Tabla de posiciones actualizada al instante, estadísticas de jugadores, posesión y próximos partidos.
- Modo "En Vivo" de baja latencia para espacios de ocio, bares deportivos y estadios.

### 4. 🎮 Sector Videojuegos & Esports
- Tableros para canales de gaming y creadores de contenido (estadísticas en vivo de Twitch/Kick/YouTube).
- Estado de servidores populares (Roblox, Minecraft), torneos e-sports y lanzamientos de la industria.

### 5. 🌌 Sector Astrología, Cultura & Estilo de Vida
- Eventos astronómicos (eclipses, lluvias de estrellas, fases lunares), efemérides y tránsitos planetarios.
- Integración con el ecosistema de experiencias luxury **Painted Leaves / Astra Novous** (voz de Sebastián, visualizaciones de audio 64b, Orrery 3D).

### 6. 🏢 Sector Retail, Hostelería & Espacios Físicos (Colombia)
- **Restaurantes y Bares**: Menús dinámicos con actualización de precios e inventario en tiempo real desde el sistema POS; estimación de tiempos de espera.
- **Universidades & Educación**: Horarios de laboratorios, eventos académicos, menú del comedor y avisos estudiantiles.
- **Hospitales & Salud**: Tiempos de espera en urgencias/consultorios, boletines de salud pública y citas.
- **Transporte Público**: Tiempos de llegada de buses (TransMilenio, SITP, Metro), estado de accesibilidad (ascensores).
- **Juntas de Acción Comunal (JAC) e Iglesias**: Anuncios comunitarios, horarios de servicios, boletines de seguridad vecinal.

---

## 🛠️ 4. Guía de Selección de Hardware & Especificaciones Técnicas

### A. Especificación de Displays y Pantallas LED (Direct View)
Basado en la *Guía de Selección de Pantallas LED*:

| Entorno / Caso de Uso | Tecnología Recomendada | Pixel Pitch (mm) | Brillo (Nits) | Grado IP |
| :--- | :--- | :--- | :--- | :--- |
| **Estudio Transmisión / Streaming 24/7** | LCD Commercial IPS / OLED | P1.5 - P2.5 | 400 - 700 nits | IP20 / IP30 |
| **Interiores Corporativos / Universidades** | LCD Comercial / LED Indoor | P1.6 - P2.5 | 500 - 1,000 nits | IP30 |
| **Vitrinas Comercial / Lobbies de Hoteles** | LED Direct View Indoor | P2.5 - P4.0 | 1,000 - 2,000 nits | IP30 / IP54 |
| **Exteriores Urbanos / Fachadas Colombia** | LED Direct View Outdoor | P4.0 - P6.0 | 4,000 - 7,000+ nits | IP65 / IP66 |

### B. Arquitectura de Cómputo Edge (Media Players)
- **Opción Estándar Recomendada**: MiniPC x86 de gama media (**Intel NUC i3/i5 o Ryzen 5**) corriendo Linux/Windows Kiosk Mode con salida HDMI limpia. Ofrece compatibilidad total con WebSockets, Canvas HTML5, Node.js y navegadores modernos.
- **Opción Económica / Despliegue Masivo**: **Raspberry Pi 4 (4GB/8GB)** con caja disipadora industrial y fuente de poder robusta para despliegues ligeros.

### C. Capa de Software & CMS
- **CMS Local / Autoalojado**: **Xibo Community Edition** (Open Source) o motor propio React/Vite para máxima flexibilidad y costo cero de licencias recurrentes.
- **SaaS Comercial**: Integración opcional con Rise Vision, ScreenCloud o Scala para clientes corporativos que requieran soporte gestionado.

---

## 🎛️ 5. Modelo de Negocio & Fuentes de Monetización

1. **Suscripción B2B por Pantalla (SaaS)**:
   - **Plan Básico**: $9.99 USD/mes por pantalla (actualizaciones estándar, plantillas base).
   - **Plan Pro**: $19.99 USD/mes por pantalla (integración de APIs en vivo, programación condicional, branding personalizado).
   - **Plan Enterprise / Marca Blanca**: $49.99+ USD/mes (multi-sitio, SLA dedicado, desarrollo de módulos a medida).
2. **Mensajes Destacados e Interactivos (Freemium / Pay-per-interaction)**:
   - Espectadores o usuarios pueden pagar una tarifa simbólica (vía WhatsApp/Stripe/MercadoPago) para proyectar mensajes, felicitaciones o anuncios destacados en la marquesina con tiempo limitado.
3. **Mercado de Módulos & Plantillas**:
   - Venta de plantillas de tableros especializadas por industria (deportes, restaurantes, eventos).
4. **Servicios de Implementación en Colombia**:
   - Paquetes de instalación, configuración de hardware, soporte y mantenimiento técnico in situ.

---

## 🚀 6. Hoja de Ruta Estratégica (Plan de 90 Días)

### Mes 1: Fundación & Motor Modular (Días 1 - 30)
- [x] Establecimiento del espacio de trabajo `Digital Signage` y sincronización P2P con la bóveda de Obsidian (`Proyectos Artist Pro/Digital Signage`).
- [ ] Construcción del **Motor de Layouts (Grid Controller)** desacoplado en React/TypeScript.
- [ ] Desarrollo de conectores genéricos para Feeds RSS y APIs de noticias/finanzas.

### Mes 2: Validación RAT & Prototipado Sectorial (Días 31 - 60)
- [ ] Ejecución del experimento RAT (medición de duración de espectador en streams con datos vivos vs estáticos).
- [ ] Construcción de prototipos para 3 verticales prioritarias: **Noticias/Política**, **Deportes/Fútbol** y **Economía**.
- [ ] Prueba de integración del canal interactivo de WhatsApp.

### Mes 3: Comercialización & Despliegue Piloto (Días 61 - 90)
- [ ] Lanzamiento de la Consola de Administración Web (`AdminConsole`) responsive con Firebase/WebSockets.
- [ ] Contacto B2B con los primeros 3 clientes piloto en Colombia (local comercial, estudio de streaming, universidad).
- [ ] Empaquetado final y manuales de operación.

---

## 🗂️ 7. Estructura de Documentación Sincronizada

```
Digital Signage/
├── README.md                                                  # Índice general del repositorio
├── PROJECT_CONTEXT.md                                         # [Este Documento Maestro Consolidado]
├── BRIEF.md                                                   # Cuestionario de descubrimiento de clientes
├── crypto-hacker-dashboard/                                   # Demo/Módulo base de referencia técnica
│
└── [Obsidian Vault/Proyectos Artist Pro/Digital Signage/]
    ├── Análisis Mercado Publicidad Pantallas Colombia.md
    ├── Guía Selección Pantallas LED Sistemas Digital Signage.md
    ├── Investigación Mercado Publicidad Pantallas Colombia.md
    ├── Pantallas comerciales.md
    ├── Tableros Inteligentes - Brief de Expansión.md
    ├── Tableros Inteligentes - Expansión de Módulos y Casos de Uso.md
    ├── Tableros Inteligentes - Resumen Integral.md
    └── Digital Signage Antigravity/                             # Espacio de trabajo de Antigravity
        ├── PROJECT_CONTEXT.md
        ├── README.md
        └── BRIEF.md
```
