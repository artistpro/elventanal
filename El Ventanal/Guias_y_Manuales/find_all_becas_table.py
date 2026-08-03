import os
import re
from pypdf import PdfReader

pdf_path = r"d:\Descargas 2\Antigravity\Digital Signage\El Ventanal\Guias_y_Manuales\Municipio de Pereira Estimulos Documentos\DECIMA QUINTA CONVOCATORIA DE ESTIMULOS PARA OBSERVACIONES.pdf"

reader = PdfReader(pdf_path)

out_path = r"d:\Descargas 2\Antigravity\Digital Signage\El Ventanal\Guias_y_Manuales\TODAS_LAS_BECAS_Y_MONTOS_PEREIRA.txt"
with open(out_path, "w", encoding="utf-8") as f:
    for i in range(35, len(reader.pages)):
        text = reader.pages[i].extract_text() or ""
        for line in text.split("\n"):
            line_str = line.strip()
            if any(k in line_str.lower() for k in ["categoría", "linea", "área", "número de estímulos", "cuantía", "valor de cada", "monto", "total", "$"]):
                f.write(f"Pág {i+1}: {line_str}\n")

print(f"Escaneo de becas completado en {out_path}")
