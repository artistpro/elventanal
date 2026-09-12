# 🌿 08. Blueprint de Replicación Paso a Paso
## Guía de Despliegue desde Cero para Nuevos Canales o Pizarras

---

## 🚀 Secuencia de Despliegue en 5 Pasos

### Paso 1: Configurar Firebase Realtime Database
1. Crear un proyecto en [Firebase Console](https://console.firebase.google.com/).
2. Crear una **Realtime Database** e importar `DEFAULT_BOARD_STATE` en `/podcast_cancer/board_state`.
3. Establecer reglas de lectura y escritura (`read: true, write: true` o con reglas protegidas).

---

### Paso 2: Clonar y Desplegar el Frontend en Vercel
```bash
git clone https://github.com/artistpro/pizarra-podcast-cancer.git
cd pizarra-podcast-cancer
npm install
npm run build
```
1. Actualizar `src/firebase.ts` con la URL de la base de datos de Firebase.
2. Conectar el repositorio de GitHub a **Vercel** para despliegue automático en `main`.

---

### Paso 3: Aprovisionar Servidor VPS Ubuntu 22.04
```bash
# 1. Instalar paquetes gráficos y de streaming
sudo apt-get update && sudo apt-get install -y \
    xvfb x11-utils xdotool ffmpeg \
    wget curl gnupg libasound2 libnss3 libatk-bridge2.0-0 libgtk-3-0

# 2. Instalar Google Chrome Stable
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo gpg --dearmor -o /usr/share/keyrings/google-chrome.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-chrome.gpg] http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.list
sudo apt-get update && sudo apt-get install -y google-chrome-stable
```

---

### Paso 4: Crear Estructura de Directorios y Audios en la VPS
```bash
mkdir -p /home/rik/streams/podcast_cancer/{logs,audio_natural,audio_solfeggio,scripts,config,chrome_profile}
```
* Subir archivos de audio ambiental (`sound.mp3` y `freq.mp3`).
* Crear entorno virtual e instalar dependencias:
  ```bash
  python3 -m venv /home/rik/streams/podcast_cancer/venv
  /home/rik/streams/podcast_cancer/venv/bin/pip install requests
  ```

---

### Paso 5: Configurar Servicios y Cronjobs
1. Crear el servicio `/etc/systemd/system/podcast_cancer_stream.service`.
2. Activar e iniciar el servicio:
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable --now podcast_cancer_stream.service
   ```
3. Añadir el cronjob de noticias con `crontab -e`:
   ```bash
   0 6,18 * * * /home/rik/streams/podcast_cancer/venv/bin/python3 /home/rik/streams/podcast_cancer/scripts/auto_news_updater.py >> /home/rik/streams/podcast_cancer/logs/news_updater.log 2>&1
   ```
