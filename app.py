import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Configuración: Base de datos y carpeta de videos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///montón.db'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # Límite de 50MB por video
db = SQLAlchemy(app)

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), default='pendiente')
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

with app.app_context():
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    db.create_all()

@app.route('/')
def index():
    return '''
    <html>
        <body style="text-align:center; font-family:Arial; padding:50px; background:#000; color:white;">
            <h1>@Para_todos1662</h1>
            <p>Sube tu video al "montón". El bot elegirá uno al azar cada 20 minutos.</p>
            <form action="/upload" method="post" enctype="multipart/form-data">
                <input type="file" name="video" accept="video/*" required><br><br>
                <button type="submit" style="background:#ff0050; color:white; border:none; padding:15px; border-radius:5px;">Enviar al Montón</button>
            </form>
        </body>
    </html>
    '''

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['video']
    if file:
        filename = f"{int(datetime.now().timestamp())}_{file.filename}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        db.session.add(Video(filename=filename))
        db.session.commit()
        return "<h1>¡Recibido! Tu video ya está en el montón.</h1><a href='/'>Subir otro</a>"
    return "Error."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
