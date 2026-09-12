# 🌿 05. Alertas en Vivo y Motor de Incentivo Comunitario (30 min)
## Sistema Reactivo y Autónomo de Reconocimiento Comunitario

---

## 🎯 1. Objetivos del Sistema de Alertas

1. **Reconocer y agradecer en tiempo real** a cada persona que se una a la comunidad de Telegram o realice una donación / regalo de YouTube.
2. **Dinamizar la pantalla de emisión continua 24/7** mediante un motor autónomo que evite pantallas estáticas cuando no haya actividad externa.
3. **Incentivar la participación** mostrando ejemplos de bienvenida y agradecimiento de forma natural y respetuosa.

---

## 🔄 2. Motor Autónomo de Incentivo Comunitario (Cada 30 Minutos)

* **Condición de Disparo**: Si transcurren **30 minutos** continuos sin que ocurra ningún evento real (nadie entra al grupo ni dona), el sistema lanza una alerta de incentivo.
* **Alternancia 1:1 (Cero Simultaneidad)**:
  * **Ciclo 1**: Bienvenida de Telegram (*Arriba a la Derecha, 9s*).
  * **Ciclo 2 (30 min después)**: Regalo / Super Chat de YouTube (*Abajo a la Izquierda, 15s*).
  * **Ciclo 3 (60 min después)**: Bienvenida de Telegram (siguiente nombre).
* **Banco de 9 Nombres Naturales**:
  1. `Claudia M.`
  2. `Carlos Andrés R.`
  3. `María Elena G.`
  4. `Patricia V.`
  5. `Fernando L.`
  6. `Luz Marina T.`
  7. `Gloria Esperanza D.`
  8. `Jorge Eduardo S.`
  9. `Martha Cecilia B.`

---

## ⭐ 3. Prioridad Absoluta de Eventos Reales

En el momento en que se detecta una entrada real en Telegram o una donación real:
1. La alerta real se muestra de inmediato en pantalla.
2. El temporizador de 30 minutos **se reinicia a cero**.
3. El nombre real queda registrado en memoria como prioridad para futuros reconocimientos comunitarios.

---

## 🎛️ 4. Control desde el Panel de Administración (`/?view=admin`)

En la **Sección 8 (Alertas & Regalos)** del panel de administración:
* **Interruptor General**: Activar / Desactivar el motor de incentivo.
* **Selector de Intervalo**: 10, 15, 20, **30** (por defecto), 45 o 60 minutos.
* **Editor de Nombres**: Modificar cualquiera de los 9 nombres del banco y botón de `↺ Restablecer 9 Nombres por Defecto`.
* **Botones de Prueba Inmediata**:
  * `🚀 Probar Bienvenida en Pantalla`
  * `🎁 Probar Alerta de Regalo / Super Chat en Pantalla`
