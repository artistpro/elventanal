# 🌿 06. Motor de Streaming en VPS & DevOps
## Servidor Xvfb, Chromium Kiosk, FFmpeg Multi-Audio y Comandos de Mantenimiento

---

## 🖥️ 1. Servidor y Entorno de Emisión

* **Servidor**: VPS Ubuntu 22.04 LTS (`217.216.48.120:2222`, usuario `rik`).
* **Directorio de Trabajo**: `/home/rik/streams/podcast_cancer/`
* **Servicio Systemd**: `podcast_cancer_stream.service`

---

## 📜 2. Script de Emisión Principal (`stream.sh`)

```bash
#!/bin/bash
export DISPLAY=:8

# 1. Iniciar servidor X virtual si no está activo
if ! pgrep -x "Xvfb" > /dev/null; then
    Xvfb :8 -screen 0 1920x1080x24 -ac +extension GLX +render -noreset &
    sleep 2
fi

# 2. Iniciar navegador Chromium en modo Kiosk
google-chrome \
    --user-data-dir=/home/rik/streams/podcast_cancer/chrome_profile \
    --kiosk \
    --no-first-run \
    --no-default-browser-check \
    --disable-translate \
    --disable-features=Translate \
    --disable-infobars \
    --disable-session-crashed-bubble \
    --disable-gpu \
    --window-size=1920,1080 \
    --window-position=0,0 \
    "https://pizarra-podcast-cancer.vercel.app/?nocache=$(date +%s)" &

sleep 5

# 3. Lanzar FFmpeg con mezcla multi-audio y captura de pantalla
ffmpeg -y \
    -f x11grab -draw_mouse 0 -framerate 30 -video_size 1920x1080 -i :8.0 \
    -thread_queue_size 1024 -re -i "http://195.26.251.31/listen/astra/radio.mp3" \
    -thread_queue_size 1024 -stream_loop -1 -re -i "/home/rik/streams/podcast_cancer/audio_natural/sound.mp3" \
    -thread_queue_size 1024 -stream_loop -1 -re -i "/home/rik/streams/podcast_cancer/audio_solfeggio/freq.mp3" \
    -filter_complex "[1:a]volume=2.0[a1]; [2:a]volume=0.3[a2]; [3:a]volume=0.11[a3]; [a1][a2][a3]amix=inputs=3:duration=first:dropout_transition=3[aout]" \
    -map 0:v -map "[aout]" \
    -c:v libx264 -preset veryfast -tune zerolatency -b:v 4500k -maxrate 4500k -bufsize 9000k \
    -pix_fmt yuv420p -g 60 -r 30 \
    -c:a aac -b:a 160k -ar 44100 \
    -f flv "rtmp://a.rtmp.youtube.com/live2/wy04-7pxe-5w3z-13dr-10a5"
```

---

## 🛠️ 3. Comandos Esenciales de Operación y Mantenimiento

### A. Recarga en Caliente de la Pizarra Web (Zero-Downtime Hot Reload):
```bash
ssh -p 2222 rik@217.216.48.120 "DISPLAY=:8 xdotool key ctrl+F5"
```

### B. Capturar Fotograma en Tiempo Real de la Emisión:
```bash
ssh -p 2222 rik@217.216.48.120 "ffmpeg -y -f x11grab -video_size 1920x1080 -i :8 -vframes 1 /tmp/live_snap.jpg"
```

### C. Gestionar el Servicio Systemd:
```bash
sudo systemctl status podcast_cancer_stream.service
sudo systemctl restart podcast_cancer_stream.service
sudo journalctl -u podcast_cancer_stream.service -f
```
