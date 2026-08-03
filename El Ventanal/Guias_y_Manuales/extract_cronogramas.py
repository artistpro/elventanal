import os
import sys
from pypdf import PdfReader

base_dir = r"d:\Descargas 2\Antigravity\Digital Signage\El Ventanal\Guias_y_Manuales"
out_file = os.path.join(base_dir, "REPORTE_CRONOGRAMAS_DOCUMENTOS_USUARIO.txt")

with open(out_file, "w", encoding="utf-8") as out:
    for root, dirs, files in os.walk(base_dir):
        for f in files:
            if f.endswith(".pdf"):
                full_path = os.path.join(root, f)
                out.write(f"\n=======================================================\n")
                out.write(f"DOCUMENTO: {f}\n")
                out.write(f"CARPETA: {os.path.basename(root)}\n")
                out.write(f"=======================================================\n")
                try:
                    reader = PdfReader(full_path)
                    out.write(f"Páginas totales: {len(reader.pages)}\n")
                    
                    full_text = ""
                    for i, page in enumerate(reader.pages):
                        t = page.extract_text() or ""
                        full_text += f"\n--- PAGINA {i+1} ---\n" + t
                        
                    lines = full_text.split("\n")
                    cron_lines = []
                    for idx, line in enumerate(lines):
                        l_lower = line.lower()
                        if any(k in l_lower for k in ["cronograma", "fecha de cierre", "fecha de apertura", "vigencia", "plazo de postula", "publicación", "resolución", "decreto", "convocatoria", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre", "2026", "2025"]):
                            # grab context around line
                            start = max(0, idx - 1)
                            end = min(len(lines), idx + 3)
                            snippet = " | ".join([lines[k].strip() for k in range(start, end) if lines[k].strip()])
                            cron_lines.append(snippet)
                            
                    out.write(f"\n--- EXTRAIDOS ({len(cron_lines)} fragmentos) ---\n")
                    for cl in cron_lines[:40]:
                        out.write(f" • {cl}\n")
                except Exception as e:
                    out.write(f"Error procesando PDF: {e}\n")

print(f"Reporte generado en: {out_file}")
