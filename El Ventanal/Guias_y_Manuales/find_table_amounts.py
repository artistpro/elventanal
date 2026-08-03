import os
from pypdf import PdfReader

pdf_path = r"d:\Descargas 2\Antigravity\Digital Signage\El Ventanal\Guias_y_Manuales\Municipio de Pereira Estimulos Documentos\DECIMA QUINTA CONVOCATORIA DE ESTIMULOS PARA OBSERVACIONES.pdf"

reader = PdfReader(pdf_path)

out_path = r"d:\Descargas 2\Antigravity\Digital Signage\El Ventanal\Guias_y_Manuales\TABLA_DETALLADA_PAGINAS_6_A_15.txt"
with open(out_path, "w", encoding="utf-8") as f:
    for p in range(5, 15):
        f.write(f"\n=========================================\n")
        f.write(f"--- PÁGINA {p + 1} ---\n")
        f.write(f"=========================================\n")
        f.write(reader.pages[p].extract_text() or "")

print(f"Guardado páginas 6 a 15 en {out_path}")
