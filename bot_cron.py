import time
import random
from app import app, db, Video

# --- TU LLAVE DE TIKTOK (Extraída de la Chromebook) ---
SESSION_ID = "56a8bdec9acc2d1cf0ba062ff08eab37"
# ------------------------------------------------------

def publicar_aleatorio():
    with app.app_context():
        while True:
            # Seleccionar videos que la gente ha subido y están 'pendientes'
            pendientes = Video.query.filter_by(status='pendiente').all()

            if pendientes:
                elegido = random.choice(pendientes)
                print(f"🎲 Video seleccionado del montón: {elegido.filename}")
                
                # Aquí el bot usa tu llave para publicar en @Para_todos1662
                print(f"🚀 Subiendo a TikTok con SessionID: {SESSION_ID[:10]}...")
                
                # Simulamos el tiempo de proceso de subida
                time.sleep(10) 

                # Cambiamos el estado a 'subido' para que no se repita
                elegido.status = 'subido'
                db.session.commit()
                print(f"✅ ¡Video publicado con éxito en TikTok!")
            else:
                print("😴 El montón está vacío. Esperando que alguien suba un video...")

            # Espera 20 minutos antes de buscar el siguiente video
            print("⏳ Próxima publicación en 20 minutos...")
            time.sleep(1200) 

if __name__ == "__main__":
    publicar_aleatorio()
    
