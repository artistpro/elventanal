import os
import time
import subprocess
from playwright.sync_api import sync_playwright

def render_presentation_video():
    video_dir = r"d:\Descargas 2\Antigravity\Digital Signage\El Ventanal\video_presentation"
    html_path = os.path.join(video_dir, "slides_template.html")
    frames_dir = os.path.join(video_dir, "frames")
    os.makedirs(frames_dir, exist_ok=True)
    
    audio_path = r"D:\Descargas 2\Antigravity\Digital Signage\El Ventanal\Rise of the Andes.mp3"
    output_mp4 = os.path.join(video_dir, "El_Ventanal_Presentacion_Oficial.mp4")
    public_mp4 = r"d:\Descargas 2\Antigravity\Digital Signage\public\El_Ventanal_Presentacion_Oficial.mp4"
    
    print("==================================================")
    print(" INICIANDO RENDERIZADO DE VIDEO EN 1080P FULL HD")
    print(f" Audio Track: {audio_path}")
    print(f" Plantilla HTML: {html_path}")
    print("==================================================")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1920, "height": 1080})
        
        file_url = f"file:///{html_path.replace(os.sep, '/')}"
        page.goto(file_url)
        page.wait_for_load_state("networkidle")
        time.sleep(1) # wait for webfonts and images
        
        slide_images = []
        num_slides = 18
        slide_duration = 9.0  # 9 seconds per slide = 162 seconds total video
        
        print(f"\nCapturando {num_slides} diapositivas en alta resolucion (1920x1080)...")
        for i in range(num_slides):
            page.evaluate(f"renderSlide({i})")
            time.sleep(0.3)
            img_path = os.path.join(frames_dir, f"slide_{i+1:02d}.png")
            page.screenshot(path=img_path)
            slide_images.append(img_path)
            print(f"  - Diapositiva {i+1:02d} / {num_slides} capturada: {os.path.basename(img_path)}")
            
        browser.close()

    print("\nGenerando secuencia de video con transiciones suavizadas via FFmpeg...")
    
    # Create input text file for ffmpeg concat with duration
    concat_txt = os.path.join(video_dir, "concat_slides.txt")
    with open(concat_txt, "w", encoding="utf-8") as f:
        for img in slide_images:
            f.write(f"file '{img.replace(os.sep, '/')}'\n")
            f.write(f"duration {slide_duration}\n")
        # repeat last frame once for ffmpeg concat requirement
        f.write(f"file '{slide_images[-1].replace(os.sep, '/')}'\n")

    video_no_audio = os.path.join(video_dir, "temp_video_no_audio.mp4")
    
    # FFmpeg command to combine slides into 30fps video
    ffmpeg_cmd_video = [
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0",
        "-i", concat_txt,
        "-vf", "fps=30,format=yuv420p",
        "-c:v", "libx264", "-preset", "fast", "-crf", "18",
        video_no_audio
    ]
    
    print(f"Ejecutando ensamblaje de video: {' '.join(ffmpeg_cmd_video)}")
    subprocess.run(ffmpeg_cmd_video, check=True)
    
    print("\nFusionando audio 'Rise of the Andes.mp3' con desvanecimiento final (Fade Out)...")
    
    # Total video duration is 18 * 9 = 162 seconds
    fade_start = 158.0
    
    ffmpeg_cmd_final = [
        "ffmpeg", "-y",
        "-i", video_no_audio,
        "-i", audio_path,
        "-c:v", "copy",
        "-c:a", "aac", "-b:a", "192k",
        "-af", f"afade=t=out:st={fade_start}:d=4",
        "-shortest",
        output_mp4
    ]
    
    print(f"Ejecutando mezcla final de audio/video: {' '.join(ffmpeg_cmd_final)}")
    subprocess.run(ffmpeg_cmd_final, check=True)
    
    # Copy to public folder for web streaming
    os.makedirs(os.path.dirname(public_mp4), exist_ok=True)
    subprocess.run(["powershell", "-Command", f"Copy-Item '{output_mp4}' '{public_mp4}' -Force"], check=True)
    
    print("\n==================================================")
    print(" RENDERIZADO COMPLETADO CON EXITO")
    print(f" Video Final: {output_mp4}")
    print(f" Enlace Publico: {public_mp4}")
    print("==================================================")

if __name__ == "__main__":
    render_presentation_video()
