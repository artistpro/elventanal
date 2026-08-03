import os
from pypdf import PdfReader

pdf_path = r"d:\Descargas 2\Antigravity\Digital Signage\El Ventanal\Guias_y_Manuales\Municipio de Pereira Estimulos Documentos\DECIMA QUINTA CONVOCATORIA DE ESTIMULOS PARA OBSERVACIONES.pdf"

reader = PdfReader(pdf_path)

out_path = r"d:\Descargas 2\Antigravity\Digital Signage\El Ventanal\Guias_y_Manuales\TABLA_ESTIMULOS_PAGINAS_5_A_35.txt"
with open(out_path, "w", encoding="utf-8") as f:
    for page_num in range(4, min(35, len(reader.pages))):
        f.write(f"\n=========================================\n")
        f.write(f"--- PÁGINA {page_num + 1} ---\n")
        f.write(f"=========================================\n")
        f.write(reader.pages[page_num].extract_text() or "")

print("Volcado de páginas 5 a 35 completado.")
