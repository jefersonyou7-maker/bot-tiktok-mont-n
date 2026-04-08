import time
import random
from app import app, db, Video

def publicar_aleatorio():
    with app.app_context():
        while True:
            # Seleccionar videos que no han sido subidos
            pendientes = Video.query.filter_by(status='pendiente').all()
            
            if pendientes:
                elegido = random.choice(pendientes)
                print(f"🎲 Seleccionado al azar: {elegido.filename}")
                
                # --- LÓGICA DE SUBIDA (Aquí conectarías con la API de TikTok) ---
                # Por ahora, simulamos la subida:
                time.sleep(5) 
                
                elegido.status = 'subido'
                db.session.commit()
                print(f"✅ Publicado en @Para_todos1662")
            else:
                print("😴 El montón está vacío. Esperando videos...")

            print("⏳ Esperando 20 minutos para el próximo video...")
            time.sleep(1200) # 1200 segundos = 20 minutos

if __name__ == '__main__':
    publicar_aleatorio()
