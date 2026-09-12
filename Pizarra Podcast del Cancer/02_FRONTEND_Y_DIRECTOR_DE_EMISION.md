# 🌿 02. Frontend y Director de Emisión
## Componentes, Modos de Bucle y Distribución Espacial Senior-Friendly

---

## 🎨 1. Filosofía de Diseño Senior-Friendly & Móvil

La interfaz visual fue rediseñada para garantizar que **adultos mayores y personas viendo la transmisión desde teléfonos móviles** puedan leer cómodamente toda la información sin forzar la vista:

1. **Modo Bucle Exclusivo de Pantallas Completas (`includeGeneralViewInLoop: false`)**:
   * La vista de 4 cuadrantes pequeños queda suspendida en el bucle automático.
   * El sistema rota permanentemente entre 4 pantallas completas de alto impacto:
     $$\text{[Noticias Full (120s)]} \longrightarrow \text{[Suplemento Full (120s)]} \longrightarrow \text{[Meditación Full (120s)]} \longrightarrow \text{[Arte \& Respiración Full (120s)]}$$
2. **Escala de Tipografías Bold**:
   * **Citas Centrales**: `4.6rem` Cinzel 900 con sombra de profundidad.
   * **Titulares de Noticias**: `3.3rem` Bold con narrativa a `1.75rem` y 4 claves a `1.45rem`.
   * **Suplementos**: Título `3.5rem` con frasco de `380px` y beneficios a `1.45rem`.
   * **Marquesinas Inferiores**: `2.25rem` Bold en blanco puro sobre fondo esmeralda oscuro de alto contraste.

---

## 🗺️ 2. Distribución Espacial en Pantalla (Cero Solapamientos)

Cada componente flotante tiene asignadas coordenadas fijas que garantizan una convivencia limpia e independiente:

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│  [🌿 EL PODCAST DEL CÁNCER V1.2]                               [TURNO NOCHE] [🔴 EN VIVO]   │
│                                                                                             │
│                                                   ┌──────────────────────────────────────┐  │
│                                                   │ 🌿 ¡BIENVENIDO(A) A LA COMUNIDAD! 🤍 │  │
│                                                   │ Claudia M. se unió a Telegram ✨     │  │
│                                                   │ [top: 88px, right: 36px] (9s)        │  │
│                                                   └──────────────────────────────────────┘  │
│                                                                                             │
│                         [ ESCENARIO CENTRAL FULL-SCREEN (620px) ]                           │
│                     (Noticias ➔ Suplemento ➔ Cita Astral ➔ Arte)                            │
│                                                                                             │
│  ┌──────────────────────────────────────┐         ┌──────────────────────────────────────┐  │
│  │ ⭐ ¡GRACIAS POR TU REGALO / APOYO! ⭐│         │ 🌿 APOYA NUESTRA COMUNIDAD           │  │
│  │ Juan Pablo R. • Super Chat $10.00    │         │ [QR] Descuento iHerb MBG0640         │  │
│  │ "Con mucho amor para la comunidad"   │         │ Cupón: MBG0640                       │  │
│  │ [bottom: 210px, left: 36px] (15s)    │         │ [bottom: 210px, right: 36px] (35s)   │  │
│  └──────────────────────────────────────┘         └──────────────────────────────────────┘  │
│ ═══════════════════════════════════════════════════════════════════════════════════════════ │
│  [ HOY RECORDAMOS ]  Eres una historia, una familia y un proyecto de vida...  (2.25rem Bold)│
│  [ INVITACIÓN ]      Te invitamos a la Comunidad. Link en la descripción...   (2.25rem Bold)│
└─────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🧩 3. Árbol de Componentes React

```
src/
├── components/
│   ├── Header.tsx                 # Cabecera fija: Título, Turno Día/Noche, Indicador EN VIVO
│   ├── BottomTicker.tsx           # Marquesinas gigantes continuas de 84px de alto (Doble tamaño)
│   ├── QrAffiliateOverlay.tsx     # Banner flotante iHerb con código QR y cupón MBG0640
│   ├── LiveAlertsOverlay.tsx      # Overlay de Bienvenidas (Telegram), Regalos (YouTube) y Motor 30 min
│   ├── LiveBoard.tsx              # Componente Master Director y Gestor de Escenas
│   ├── admin/
│   │   └── AdminConsole.tsx       # Panel de control de emisión con control 1-Click
│   └── fullscreen/
│       ├── FullScreenNews.tsx        # Ficha 620px: Titular 3.3rem, Narrativa 1.75rem, 4 Claves 1.45rem
│       ├── FullScreenSupplement.tsx  # Ficha 620px: Frasco 380px, Título 3.5rem, Sinergias y Beneficios
│       ├── FullScreenAstral.tsx      # Ficha 620px: Cita Gigante 4.6rem Cinzel 900 con Geometría Sagrada
│       └── FullScreenArt.tsx         # Ficha 620px: Marco Museo 520px, Título 3.4rem, Esfera 110px 4x4
```

---

## ⚙️ 4. Marquesinas Continuas Asíncronas (`BottomTicker.tsx`)

* **Estructura Doble**:
  * Barra 1: `HOY RECORDAMOS` (Frases de empoderamiento, testimonios y recordatorios diarios).
  * Barra 2: `INVITACIÓN` (Llamados a la acción para la comunidad de Telegram y consulta médica).
* **Dimensiones**: Altura de `84px` por barra (total ~`180px`), insignias de `340px` de ancho con tipografía `1.45rem`.
* **Velocidad de Desplazamiento**: Ciclos ultra lentos y continuos (6.5 a 8 minutos por ciclo completo) para lectura pausada y relajante.
