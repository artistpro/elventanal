import os
from pypdf import PdfReader

pdf_path = r"d:\Descargas 2\Antigravity\Digital Signage\El Ventanal\Guias_y_Manuales\Municipio de Pereira Estimulos Documentos\DECIMA QUINTA CONVOCATORIA DE ESTIMULOS PARA OBSERVACIONES.pdf"

reader = PdfReader(pdf_path)
full_text = ""
for i, p in enumerate(reader.pages):
    full_text += f"\n--- PAGINA {i+1} ---\n" + (p.extract_text() or "")

lines = full_text.split("\n")
budget_lines = []
for idx, line in enumerate(lines):
    l_lower = line.lower()
    if any(k in l_lower for k in ["cuanto", "cuantía", "monto", "valor", "máximo", "estímulo", "bolsa", "cuantía de los estímulos", "presupuesto de la convocatoria", "pesos", "$"]):
        start = max(0, idx - 1)
        end = min(len(lines), idx + 3)
        snippet = " | ".join([lines[k].strip() for k in range(start, end) if lines[k].strip()])
        budget_lines.append((idx, snippet))

print(f"Total coincidencias de presupuesto: {len(budget_lines)}")
for idx, snippet in budget_lines[:50]:
    print(f"Línea {idx}: {snippet}")
