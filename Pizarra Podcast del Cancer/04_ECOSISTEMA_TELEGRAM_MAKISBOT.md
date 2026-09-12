# 🌿 04. Ecosistema Telegram & Makix Bot
## Integración en Desktop Linux (`192.168.1.94`) con la Transmisión en Vivo

---

## 🖥️ 1. Entorno de Ejecución en Desktop Linux

* **Host**: Desktop Linux de Estudio / Casa (`192.168.1.94`, usuario `remoto`).
* **Directorio**: `/home/remoto/podcast_cancer_bot/`
* **Entorno Virtual**: `/home/remoto/podcast_cancer_bot/venv/`
* **Servicio Systemd**: `podcast-cancer-bot.service`
* **Acceso SSH**: `ssh -i ~/.ssh/id_ed25519 remoto@192.168.1.94`

---

## 🤖 2. Comandos y Funcionalidades del Bot

1. `/protocolo`: Envía el protocolo completo y pautas de acompañamiento.
2. `/recomendacion`: Comparte un video de Odysee o YouTube seleccionado para la comunidad.
3. `/videos`: Lista de contenidos recientes.
4. `/historia`: Relato del origen, misión y valores de El Podcast del Cáncer.
5. `/reglas`: Pautas de respeto y convivencia del grupo.

---

## ⚡ 3. Webhook en Tiempo Real para Bienvenidas (`welcome_new_member`)

En el archivo `/home/remoto/podcast_cancer_bot/bot.py`, cuando un nuevo miembro ingresa al grupo de Telegram:

```python
async def welcome_new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        if member.is_bot:
            continue
        
        name = member.first_name or "Amigo/a de la Comunidad"
        
        # 1. Saludo cálido en el grupo público de Telegram
        welcome_text = (
            f"🌿 *¡Bienvenido(a), {name}, a El Podcast del Cáncer!* 🤍\n\n"
            "Este es un espacio de luz, ciencia, esperanza y acompañamiento mutuo."
        )
        await update.message.reply_text(welcome_text, parse_mode="Markdown")
        
        # 2. Inyección asíncrona a Firebase para la burbuja en pantalla en YouTube
        send_live_welcome_alert(name)
```

### Función de Envío a Firebase:
```python
def send_live_welcome_alert(name: str):
    try:
        url = "https://dashboard-bch-default-rtdb.firebaseio.com/podcast_cancer/live_alerts/latest.json"
        payload = {
            "id": f"welcome_{int(time.time() * 1000)}",
            "type": "welcome",
            "title": "¡BIENVENIDO(A) A LA COMUNIDAD!",
            "name": name,
            "subtitle": "se unió a nuestro Telegram de apoyo y vida 🤍",
            "timestamp": int(time.time() * 1000),
            "durationSec": 9
        }
        requests.put(url, json=payload, timeout=5)
    except Exception as e:
        print(f"Error enviando alerta a Firebase: {e}")
```

---

## 🛡️ 4. Protocolo de Cero Spam en el Grupo

* **Regla Inflexible**: Queda prohibido enviar mensajes de simulación o pruebas al grupo público de Telegram.
* **Pruebas Seguras**: Las pruebas de alertas se realizan directamente desde la **Sección 8 del Panel Admin (`/?view=admin`)**, inyectando la señal a Firebase sin molestar a los usuarios del grupo.
