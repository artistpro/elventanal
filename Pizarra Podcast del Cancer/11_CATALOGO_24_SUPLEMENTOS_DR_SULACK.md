# 11. Catálogo Maestro de 24 Suplementos (Dr. Pete Sulack) & Blindaje de Imágenes

## 1. Visión General y Fundamento Clínico
El módulo **"Suplementos y Evidencia"** de la Pizarra Digital 24/7 de *El Podcast del Cáncer* tiene como objetivo educar y acompañar a pacientes y familiares con fichas técnicas rigurosas, serenas y fundamentadas en evidencia científica y medicina integrativa.

Para elevar radicalmente la profundidad del contenido y evitar la repetición monótona de 4 a 8 elementos básicos, se diseñó un catálogo maestro de **24 variantes clínicas** extraídas directamente del **Protocolo de Resiliencia del Dr. Pete Sulack** (*Dra. Pete Sulack Podcast del Cáncer / Protocolo Dr. Pete*) y de la literatura moderna en oncología metabólica.

---

## 2. Los 4 Bloques Funcionales (24 Variantes Clínicas)

### Bloque A: Respiración Mitocondrial y Energía Celular (6 Suplementos)
Centrado en restaurar el metabolismo mitocondrial, modular la fosforilación oxidativa y combatir la astenia/fatiga severa:
1. **Azul de Metileno (Grado USP):** Aceptor y donante catalítico de electrones a nivel del complejo IV mitocondrial; optimiza el consumo celular de oxígeno.
2. **Coenzima Q10 (Ubiquinol) + PQQ:** Estimula la biogénesis mitocondrial de organelos nuevos y sanos, protegiendo lípidos de membrana celular.
3. **Vitamina C Intravenosa / Liposomal:** Pro-oxidante selectivo en células desdiferenciadas mediante generación de peróxido de hidrógeno; soporte estructural tisular.
4. **Glutatión Liposomal + NAC:** El antioxidante maestro intracelular; regenera la capacidad detoxificante hepática y neutraliza especies reactivas sin entorpecer la fisiología.
5. **Acetil L-Carnitina (ALCAR) + Ácido Alfa Lipoico (ALA):** Lanzadera de ácidos grasos hacia la matriz mitocondrial; regenera cofactores metabólicos y protege fibras nerviosas.
6. **Magnesio Malato & Taurato:** Soporte directo a la enzima ATP sintasa mitocondrial; promueve la relajación del músculo liso y función cardiovascular.

### Bloque B: Inmunidad y Oncología Metabólica (6 Suplementos)
Basado en restricción metabólica, señalización celular y apoptosis selectiva:
7. **Berberina HCL (Activador AMPK):** Mimetizador de restricción calórica; activa la cinasa AMPK y modula la vía mTOR/sensibilidad a la insulina periférica.
8. **Extracto de Té Verde (EGCG Fitosomado):** Polifenol con alta actividad antiangiogénica; inhibe receptores de factores de crecimiento endotelial (VEGF).
9. **Curcumina Fitosomada (Meriva):** Potente inhibición de la cascada NF-kB y citocinas proinflamatorias (IL-6, TNF-alfa); mejora biodisponibilidad por fosfolípidos.
10. **Complejo de Hongos Medicinales (Reishi, Cordyceps, PSK, Melena de León):** Beta-glucanos 1,3/1,6 inmunomoduladores que incrementan la actividad de células Natural Killer (NK) y macrófagos.
11. **Aceite de Semilla Negra (Timokinona Prensada en Frío):** Modulación de vías apoptóticas e inhibición del estrés oxidativo mitocondrial patológico.
12. **Graviola (Extracto Estandarizado de Acetogeninas):** Fitoquímica vegetal tradicional orientada a la modulación energética mitocondrial.

### Bloque C: Genética, Metilación y Terreno Biológico (6 Suplementos)
Enfocado en cofactores esenciales para la reparación del ADN, estabilidad epigenética y homeostasis mineral:
13. **Complejo B Metilado (Metilfolato 5-MTHF + Metilcobalamina):** Soporte indispensable a las vías de metilación celular, ciclo de un carbono y eliminación de homocisteína.
14. **Vitamina D3 + K2 (MK-7 Liposoluble):** Hormona esteroidea inmunomoduladora clave; la vitamina K2 guía el calcio hacia los depósitos óseos previniendo calcificaciones.
15. **Magnesio Bisglicinato:** Alta biodisponibilidad y quelación con glicina; reduce el cortisol y el hipertono del sistema nervioso simpático.
16. **Omega-3 IFOS (Alta Concentración EPA/DHA):** Resolución de procesos inflamatorios crónicos tisulares mediante mediadores pro-resolutivos (SPMs).
17. **Cardo Mariano (Silibinina Fitosomada):** Protección del hepatocito frente a sobrecarga química y soporte a la síntesis de bilis y glutatión.
18. **Selenio (Selenometionina) + Zinc Bisglicinato:** Minerales traza indispensables para las enzimas antioxidantes selenoproteínas y superóxido dismutasa (SOD).

### Bloque D: Eje Intestino-Cerebro, Detoxificación y Fitoquímica (6 Suplementos)
Enfocado en la barrera intestinal, ritmo circadiano, drenaje de toxinas y senolisis:
19. **Melatonina de Alta Dosis (Grado Médico):** Regulador maestro circadiano y antioxidante intracelular específico de la matriz mitocondrial.
20. **Probióticos Multicepa + Prebióticos:** Restablecimiento de la eubiosis intestinal, soporte al GALT y producción de ácidos grasos de cadena corta (butirato).
21. **L-Glutamina & Colágeno Hidrolizado:** Reparación de uniones estrechas del epitelio intestinal (barrera contra translocación bacteriana).
22. **Calostro Bovino (Factores de Transferencia e Inmunoglobulinas):** Memoria inmunológica oral y bioactivos inmunoestimulantes para la mucosa digestiva.
23. **Zeolita Micronizada (Clinoptilolita) + Carbón Activado:** Quelación pasiva gastrointestinal de endotoxinas sin absorberse a nivel sistémico.
24. **Resveratrol Trans + Quercetina:** Activadores de la vía de las sirtuinas (SIRT1) y polifenoles senolíticos para depuración biológica.

---

## 3. Blindaje Triple de Imágenes (Solución a Fallos Visuales)

### Diagnóstico del Problema Histórico:
En versiones anteriores, las tarjetas de suplementos (`SupplementCard.tsx` y `FullScreenSupplement.tsx`) contenían un manejador de error reactivo destructivo:
```tsx
// ❌ CÓDIGO ANTERIOR CON BUG VISUAL:
onError={(e) => { (e.target as HTMLElement).style.display = 'none'; }}
```
Cualquier fluctuación de red, bloqueo temporal o latencia de CDN provocaba que el elemento `<img>` se ocultara por completo, dejando un contenedor vacío o deformado en la transmisión en directo.

### Solución Arquitectónica Implementada:
1. **Fallback Resiliente de Alta Disponibilidad:** Se declaró una imagen universal de frascos de laboratorio y formulaciones botánicas (`FALLBACK_SUPPLEMENT_IMAGE`) alojada en CDN optimizado con compresión WebP.
2. **Reemplazo Dinámico en Vivo (No Destructivo):**
```tsx
// ✅ CÓDIGO BLINDADO (v1.7):
onError={(e) => {
  const target = e.target as HTMLImageElement;
  if (target.src !== FALLBACK_SUPPLEMENT_IMAGE) {
    target.src = FALLBACK_SUPPLEMENT_IMAGE;
  }
}}
```
3. **Cero Pantallas Vacías:** Si la URL original falla, conmuta silenciosamente en 1 frame al fallback sin alterar la geometría de la tarjeta ni ocultar el texto.

---

## 4. Algoritmo de Rotación Diaria (Sliding Window)

Para asegurar que la pantalla siempre muestre contenido fresco y variado sin saltos bruscos:
- Cada día a las **00:00 UTC**, el pipeline calcula el índice del día del año:
  $$\text{startIndex} = (\text{día\_del\_año} \times 2) \pmod{24}$$
- Se extraen **4 suplementos** contiguos del banco maestro de 24:
  $$\text{activos} = [\text{banco}[(\text{startIndex} + i) \pmod{24}] \quad \text{para } i \in \{0, 1, 2, 3\}]$$
- **Efecto de Transición Suave:** Al desplazarse 2 posiciones diarias, el carrusel conserva 2 suplementos del día anterior y añade 2 completamente nuevos. El ciclo completo recorre los 24 suplementos cada 12 días de manera continua y armónica.

---

## 5. Automatización VPS y Control Administrativo

### Sincronización Automática Diaria (VPS 1):
- **Script:** `/home/rik/streams/podcast_cancer/scripts/auto_supplement_updater.py`
- **Cronjob:** `0 0 * * *` (todos los días a medianoche)
- **Destino Firebase RTDB:**
  - `podcast_cancer/board_state/supplementsList.json` (4 fichas completas para el carrusel)
  - `podcast_cancer/board_state/supplement.json` (ficha destacada con compatibilidad hacia atrás)

### Control Manual en 1-Clic (`AdminConsole.tsx`):
En la Sección 5 (*"Catálogo Rotativo de Suplementos"*):
1. **Botón *"✨ Sincronizar Fichas de Hoy (4 Activas)"*:** Calcula el día actual y aplica la rotación matemática al instante.
2. **Botón *"📚 Cargar las 24 Variantes"*:** Despliega todo el arsenal de 24 fichas de golpe para eventos especiales o revisión completa.
