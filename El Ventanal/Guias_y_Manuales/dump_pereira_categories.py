import os
from pypdf import PdfReader

pdf_path = r"d:\Descargas 2\Antigravity\Digital Signage\El Ventanal\Guias_y_Manuales\Municipio de Pereira Estimulos Documentos\DECIMA QUINTA CONVOCATORIA DE ESTIMULOS PARA OBSERVACIONES.pdf"

reader = PdfReader(pdf_path)
full_text = ""
for i, p in enumerate(reader.pages):
    full_text += f"\n--- PAGINA {i+1} ---\n" + (p.extract_text() or "")

out_path = r"d:\Descargas 2\Antigravity\Digital Signage\El Ventanal\Guias_y_Manuales\CATEGORIAS_Y_CUANTIAS_PEREIRA.txt"
with open(out_path, "w", encoding="utf-8") as f:
    lines = full_text.split("\n")
    for idx, line in enumerate(lines):
        l_lower = line.lower()
        if any(k in l_lower for k in ["beca", "premio", "estímulo", "monto", "cuantía", "pesos", "$", "artes visuales", "nuevos medios", "innovación", "tecnología", "producción"]):
            f.write(f"Línea {idx}: {line.strip()}\n")

print(f"Búsqueda guardada en {out_path}")
