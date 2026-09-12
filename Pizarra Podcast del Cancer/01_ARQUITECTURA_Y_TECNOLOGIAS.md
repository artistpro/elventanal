# 🌿 01. Arquitectura Global y Stack Tecnológico
## Ecosistema Distribuido Multi-Host "El Podcast del Cáncer"

---

## 🏗️ 1. Diagrama de Arquitectura Global

El sistema opera bajo un modelo distribuido desacoplado entre **3 entornos físicos/virtuales** interconectados mediante WebSockets y APIs REST:

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                ARQUITECTURA GENERAL DEL SISTEMA                                 │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘

  [1. DESKTOP LINUX CASA (192.168.1.94)]           [2. CRON VPS / SERVICIOS EXTERNOS]
  ────────────────────────────────────             ──────────────────────────────────
   Makix Bot (Telegram @podcasdelcancer)            auto_news_updater.py (ScienceDaily + DeepSeek)
   • Evento: welcome_new_member                     • Se ejecuta a las 06:00 y 18:00
   • Saludo en grupo público Telegram               • Procesa titular, síntesis y 4 claves
   • Inyección asíncrona a Firebase                 • Inyección a /board_state/goodNews.json
                    │                                                      │
                    ▼                                                      ▼
    ┌─────────────────────────────────────────────────────────────────────────────┐
    │                 FIREBASE REALTIME DATABASE (dashboard-bch)                  │
    │  • /podcast_cancer/board_state.json        (Configuración y Contenidos)     │
    │  • /podcast_cancer/live_alerts/latest.json (Alertas de Bienvenida/Regalos)  │
    └─────────────────────────────────────────────────────────────────────────────┘
                                            │
                                            ▼ (WebSocket Listener en Tiempo Real)
                            [3. PIZARRA WEB EN VERCEL (PROD)]
                      (https://pizarra-podcast-cancer.vercel.app)
                                            │
                                            ▼ (Render KIOSK 1920x1080)
                       [4. SERVIDOR VPS (217.216.48.120:2222)]
                                     [DISPLAY=:8]
                                            │
   [Astra Radio Online Stream] ──────────┐  │ (Captura x11grab @ 30 FPS)
   [Audio Naturaleza Loop]     ──────────┼──┴────────> [FFmpeg 7+ Multi-Audio Mixer]
   [Audio Solfeggio 432Hz]     ──────────┘                      │
                                                                ▼ (RTMP H.264 / AAC)
                                                    [YOUTUBE LIVE STREAM 24/7]
                                                    (ID de Emisión: 5rJBvQM8hjk)
```

---

## 🛠️ 2. Stack Tecnológico

### A. Frontend & Renderizado Web:
* **React 19 + TypeScript + Vite 8**: SPA de alto rendimiento, modular, tipado estricto.
* **Tipografía Senior-Friendly**: Fuentes `Cinzel` (titulares y nombres) e `Inter` (cuerpo de texto y claves) con escala aumentada (+30% a +80%).
* **Canvas API HTML5**: Fondo interactivo con partículas estelares flotantes y geometría sagrada animada con rotación continua.
* **qrcode.react**: Generación de códigos QR vectoriales nítidos con corrección de error nivel Q.

### B. Backend & Sincronización:
* **Firebase Realtime Database**: Base de datos NoSQL ultra-ligera basada en WebSockets con latencia `< 150ms`.
* **Vercel**: Alojamiento y despliegue continuo (CI/CD) conectado a GitHub (`main`).

### C. Inteligencia Artificial & Fuentes de Datos:
* **DeepSeek AI (`deepseek-chat`)**: Modelo LLM para procesar artículos científicos, traducir al español, redactar con enfoque esperanzador y generar 4 claves de salud integral.
* **RSS Feeds Médicos**: *ScienceDaily Oncology & Cancer Research*.
* **OpenGraph Scraper**: Extracción automática de fotografías oficiales de los artículos.

### D. Servidor VPS & Streaming:
* **Ubuntu Linux 22.04 LTS** (`217.216.48.120:2222`).
* **Xvfb**: Servidor gráfico virtual en memoria (`DISPLAY=:8`) a resolución fija `1920x1080x24`.
* **Google Chrome**: Modo `--kiosk --no-first-run --disable-gpu` apuntando a la Pizarra.
* **FFmpeg 7+**: Captura `x11grab` y mezclador de 3 pistas de audio concurrentes (Radio Online + Naturaleza + Solfeggio 432Hz).
* **Systemd**: Demonio de servicio `podcast_cancer_stream.service`.

### E. Ecosistema Telegram:
* **Desktop Linux Ubuntu** (`192.168.1.94`, usuario `remoto`).
* **Python Telegram Bot v20+** con arquitectura `asyncio`.
* **Demonio Systemd**: `podcast-cancer-bot.service`.
