# 🌿 03. Motor Autónomo de Noticias Diarias con IA
## Pipeline de IA DeepSeek, Fuentes Nativas en Español y Blindaje Lingüístico (v1.6)

---

## ⚙️ 1. Flujo del Pipeline de Procesamiento

El script `/home/rik/streams/podcast_cancer/scripts/auto_news_updater.py` se ejecuta de forma autónoma dos veces al día en la VPS (`06:00` y `18:00`):

```
[Pool Multifuente Nativo en Español]
(EFE Salud, Infosalus, Gaceta Médica, Noticias Positivas)
          │
          ▼ (Descarga XML/RSS)
[Filtro Anti-Repetición] ──> ¿URL ya procesada en news_history.json? ──> Sí ➔ Descartar
          │ (No)
          ▼
[Filtro Anti-Alarmismo y YouTube Advertiser-Safe]
• Lista negra: mortalidad, letal, muerte, sexualidad, términos quirúrgicos íntimos
• Relevancia médica: nutrición, biología celular, medicina integrativa, bienestar
          │ (Pasa filtros)
          ▼
[Verificación de Presupuesto (Regla 12 - Budget Guard)]
• Límite: Máx. 10 llamadas/día a DeepSeek en .news_budget_ledger.json
• Disyuntor: Si falla 3 veces consecutivas ➔ Conmuta a Banco Curado de 24 Referencias
          │ (Presupuesto OK)
          ▼
[DeepSeek AI API (deepseek-chat)]
• Tono cálido, esperanzador, espiritual y riguroso
• Titular conciso (máx. 12 palabras) y síntesis en español (máx. 200 caracteres)
• 4 Claves de salud accionables enriquecidas con emojis
          │
          ▼
[Validador Lingüístico Determinista: is_spanish_text()]
¿100% Español sin tecnicismos en inglés?
          ├── No ➔ Descarte inmediato y sustitución por Banco Curado Local
          └── Sí ➔ Continuar
          │
          ▼
[Inyección REST a Firebase RTDB]
(PUT https://dashboard-bch-default-rtdb.firebaseio.com/podcast_cancer/board_state/goodNews.json)
          │
          ▼
[Actualización Instantánea en Pantalla de YouTube sin Reiniciar el Stream]
```

---

## 🛡️ 2. Medidas de Blindaje Editorial y Lingüístico

1. **Tolerancia Cero al Inglés (`is_spanish_text`):**  
   Auditoría de palabras vacías (*stopwords*) y patrones lingüísticos en español. Si una fuente externa o la IA intentan filtrar oraciones en inglés, el contenido se neutraliza y se reemplaza automáticamente por una monografía clínica del banco curado local.

2. **Banco Curado de 24 Monografías Clínicas (Fallback Resiliente):**  
   Banco permanente de 24 revisiones médicas (inmunoterapia, micoterapia, melatonina en alta dosis, cronobiología celular, bioenergética, azul de metileno, coherencia cardíaca, etc.). Rota mediante `(día_del_año * 4) % 24`, garantizando un mes completo de noticias frescas sin coste de red ni repetición.

3. **Blindaje contra Sanciones de YouTube (Advertiser-Safe):**  
   Filtro estricto que elimina referencias a temáticas íntimas, anatómicas o cirugías explícitas, enfocando el canal en esperanza, amor, fe, espiritualidad y hábitos saludables de vida.

4. **Salvaguarda de Costo y Disyuntor (Regla 12):**  
   Ledger atómico `.news_budget_ledger.json` con tope de 10 peticiones diarias. Si el servicio se interrumpe, el disyuntor salta y activa el fallback local sin interrumpir la emisión en vivo.

---

## 🤖 3. Prompt del Sistema para DeepSeek AI

```python
system_prompt = (
    "Eres un editor científico, médico y divulgador de oncología integrativa y medicina del estilo de vida. "
    "Tu misión es resumir noticias y avances biomédicos para pacientes y familiares con un enfoque de "
    "esperanza activa, rigor, serenidad, amor y vitalidad biológica. "
    "IMPORTANTE: Prohibido usar tono alarmista, lúgubre o palabras de muerte/fatalidad. "
    "Prohibido tocar temas sexuales, genitales o procedimientos quirúrgicos explícitos. "
    "Enfócate en nutrición, inmunología, bienestar celular, mente, ejercicio, descanso y avances científicos. "
    "TODO EL CONTENIDO DEBE ESTAR ESTRICTAMENTE EN ESPAÑOL IMPECABLE.\n"
    "Estructura JSON requerida:\n"
    "- title: Titular en español (máx 12 palabras, mayúsculas sobrias)\n"
    "- summary: Síntesis esperanzadora y clara en español (máx 200 caracteres)\n"
    "- category: Categoría (ej. BIENESTAR Y SALUD, AVANCES BIOMÉDICOS, INMUNOLOGÍA, ESPERANZA ACTIVA)\n"
    "- keyPoints: Exactamente 4 claves prácticas y rigurosas con emoji inicial"
)
```

---

## ⏰ 4. Programación en Cron (`crontab -l` en VPS 1)

```bash
0 6,18 * * * /home/rik/streams/podcast_cancer/venv/bin/python3 /home/rik/streams/podcast_cancer/scripts/auto_news_updater.py >> /home/rik/streams/podcast_cancer/logs/news_updater.log 2>&1
```

* **06:00 AM:** Actualización y publicación del paquete de noticias matutino.
* **06:00 PM:** Actualización y publicación del paquete de noticias vespertino.
