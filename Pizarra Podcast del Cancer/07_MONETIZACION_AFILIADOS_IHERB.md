# 🌿 07. Sistema de Monetización con Afiliados iHerb
## Estrategia de Comisiones con Cupón MBG0640 y Categorías Evergreen

---

## 💊 1. Estrategia del Cupón de Recompensas

* **Código de Afiliado**: `MBG0640`
* **Beneficio para la Audiencia**: Ofrece entre **5% y 10% de DESCUENTO** directo en cualquier compra realizada en iHerb a nivel global.
* **Propósito**: Sostener económicamente los servidores, el podcast y los espacios comunitarios de forma transparente y ética.

---

## 🔗 2. Enlaces por Categorías Globales Evergreen

Para evitar que los enlaces se rompan o los productos específicos se agoten en países particulares, todos los enlaces y códigos QR apuntan a las categorías maestras oficiales con el cupón pre-aplicado:

| Suplemento | Enlace Oficial con Descuento |
| :--- | :--- |
| **Glicinato de Magnesio** | `https://www.iherb.com/c/magnesium-glycinate?rcode=MBG0640` |
| **Vitamina D3** | `https://www.iherb.com/c/vitamin-d?rcode=MBG0640` |
| **Omega 3 (EPA/DHA)** | `https://www.iherb.com/c/omega-3-fish-oil?rcode=MBG0640` |
| **Curcumina Fitosomada** | `https://www.iherb.com/c/curcumin?rcode=MBG0640` |
| **Probióticos y Microbiota** | `https://www.iherb.com/c/probiotics?rcode=MBG0640` |

---

## 📱 3. Overlay Flotante con Código QR (`QrAffiliateOverlay.tsx`)

* **Ubicación**: `bottom: 210px, right: 36px` (no solapa con noticias, marquesinas, alertas ni regalos).
* **Modo de Visualización**:
  * **Periódico (Por Defecto)**: Aparece cada 10 minutos (600s) durante 35 segundos.
  * **Fijo Permanente**: Disponible desde el panel de control.
* **Render Vectorial**: Genera el código QR nítido con corrección de error nivel Q para escaneo instantáneo desde la pantalla de TV o teléfono.
