# 🎨 09. Galería Dinámica "Arte Que Sana"
## Rotación Continua 24h, Balance Comunidad/Maestros y Meditación Visual 4x4 (v1.6)

---

## 🏛️ 1. Filosofía y Enfoque Editorial

El módulo **"Arte Que Sana"** funciona como un ancla visual y terapéutica dentro de la emisión continua 24/7 en YouTube (`wy04-7pxe-5w3z-13dr-10a5`). Su objetivo no es la mera ornamentación, sino inducir estados neurobiológicos de calma, reducir la sobreactivación del eje hipotálamo-hipofisario-adrenal (HPA) y disminuir el cortisol en pacientes y familiares en tratamiento oncológico.

### Pilares Fundamentales:
* **Humanización del Dolor y Esperanza:** 50% de las obras provienen directamente de pacientes, sobrevivientes y cuidadores de iniciativas de arte-terapia (*Brushes with Cancer, Lilly Oncology on Canvas, Arts in Medicine*).
* **Trascendencia y Belleza Universal:** 50% de las obras pertenecen a grandes maestros impresionistas y paisajistas de la luz (Claude Monet, Vincent van Gogh, Gustav Klimt, J.M.W. Turner, Camille Corot, Albert Bierstadt).
* **Blindaje YouTube Live (Zero Strikes):** Curaduría con cero desnudez clásica ni contemporánea, cero temas anatómicos ambiguos y cero imágenes de cirugías o heridas.

---

## ⚙️ 2. Algoritmo de Ventana Deslizante (Sliding Window)

Para evitar la monotonía sin generar saltos abruptos en la mente del espectador habitual:

* **Banco Maestro de 40 Obras:**
  - 20 Obras de la Comunidad con historias reales de superación y bio-reflexiones.
  - 20 Obras de Grandes Maestros enfocadas en agua serena, luz matutina, bosques y flores.
* **Galería Activa en Emisión:** Exactamente **8 obras simultáneas** entrelazadas de forma armónica:
  `[Comunidad, Maestro, Comunidad, Maestro, Comunidad, Maestro, Comunidad, Maestro]`.
* **Fórmula Matemática Diaria:**
  $$\text{offset} = (\text{día\_del\_año} \times 2) \pmod{20}$$
* **Dinámica de Renovación a las 00:00:**
  - Se descartan las 4 obras más antiguas de la jornada anterior.
  - Se incorporan **4 obras nuevas** (2 de comunidad + 2 de grandes maestros).
  - Se conservan **4 obras** del día previo (efecto carrusel suave).
  - Produce un ciclo continuo de 10 días sin combinaciones idénticas.

---

## 🧘 3. Experiencia en Pantalla Completa y Respiración 4x4

Cuando el director de emisión o el bucle automático activa el modo pantalla completa (`FullScreenArt.tsx`):

1. **Marco Clásico de Museo (620px):** Diseño refinado con degradados oscuros, bordes dorados (#d4af37) y relieve tridimensional.
2. **Ficha Clínica y Testimonial:** Título, autor/movimiento y reflexión sobre el impacto neurobiológico del arte contemplativo.
3. **Guía de Respiración Guiada 4x4 (Cadencia de 16 Segundos):**
   - 🌿 **Fase 1: Inhala Profundo (4s)** — *Llénate de calma, oxígeno y serenidad interior.* (Verde esmeralda `#6ee7b7`, escala 1.25).
   - 🌿 **Fase 2: Retén el Aire (4s)** — *Siente la quietud y plenitud en tu centro.* (Dorado suave `#fef08a`, escala 1.25).
   - 🌿 **Fase 3: Exhala Despacio (4s)** — *Suelta toda tensión, dolor y preocupación.* (Azul cielo `#93c5fd`, escala 0.85).
   - 🌿 **Fase 4: Paz y Gratitud (4s)** — *Descansa en tu fuerza vital y esperanza.* (Oro radiante `#d4af37`, escala 0.85).

---

## 🖥️ 4. Automatización y DevOps en Servidor

### Script Autónomo en VPS 1:
* **Ruta:** `/home/rik/streams/podcast_cancer/scripts/auto_art_updater.py`
* **Intérprete:** `/home/rik/streams/podcast_cancer/venv/bin/python3`
* **Cronjob Activo (`crontab -l`):**
  ```bash
  0 0 * * * /home/rik/streams/podcast_cancer/venv/bin/python3 /home/rik/streams/podcast_cancer/scripts/auto_art_updater.py >> /home/rik/streams/podcast_cancer/logs/art_updater.log 2>&1
  ```
* **Destino REST:**
  `PUT https://dashboard-bch-default-rtdb.firebaseio.com/podcast_cancer/board_state/artCards.json`

### Control Web Interactivo (Admin Console):
* En `AdminConsole.tsx`, el botón `✨ Sincronizar Galería de Hoy (8 Obras)` permite invocar directamente `getDailyArtGallery()` desde `src/services/artService.ts` y persistirlo en Firebase RTDB con un solo clic.
