import os
import re
from pypdf import PdfReader

def parse_pdf(filepath):
    print(f"\n==========================================")
    print(f"ANALIZANDO: {os.path.basename(filepath)}")
    print(f"Ruta: {filepath}")
    print(f"==========================================")
    
    try:
        reader = PdfReader(filepath)
        num_pages = len(reader.pages)
        print(f"Total Páginas: {num_pages}")
        
        full_text = ""
        for i, page in enumerate(reader.pages):
            text = page.extract_text() or ""
            full_text += f"\n--- PÁGINA {i+1} ---\n" + text
            
        # Search for key sections: cronograma, fechas, cierres, convocatoria, montos
        keywords = ["cronograma", "fecha", "cierre", "apertura", "plazo", "postulaci", "vigencia", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre", "términos", "monto", "presupuesto"]
        
        matches = []
        for line in full_text.split("\n"):
            line_lower = line.lower()
            if any(kw in line_lower for kw in keywords):
                if len(line.strip()) > 5:
                    matches.append(line.strip())
                    
        print(f"\n--- FRAGMENTOS CLAVE ENCONTRADOS ({len(matches)} líneas) ---")
        for m in matches[:35]: # show first 35 key matches
            print(f" • {m}")
            
        return full_text
    except Exception as e:
        print(f"Error analizando {filepath}: {e}")
        return ""

def main():
    base_dir = r"d:\Descargas 2\Antigravity\Digital Signage\El Ventanal\Guias_y_Manuales"
    
    pdf_files = []
    for root, dirs, files in os.walk(base_dir):
        for f in files:
            if f.endswith(".pdf"):
                pdf_files.append(os.path.join(root, f))
                
    print(f"Encontrados {len(pdf_files)} archivos PDF para analizar.")
    
    results = {}
    for pdf_path in pdf_files:
        text = parse_pdf(pdf_path)
        results[os.path.basename(pdf_path)] = text

if __name__ == "__main__":
    main()
