from src.app import app
import os
from flask import Flask, flash, request, render_template, redirect
from werkzeug.utils import secure_filename
from src.predictions_api import *

UPLOAD_FOLDER = './src/controllers/upload_biopsy'
ALLOWED_EXTENSIONS = {'jpg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.secret_key = "super secret key"

@app.route("/")
def askFile():
    return render_template('web.html')


@app.route('/diagnosis', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['myFile']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        imagen = load_reshape_image(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        prediccion = predictNewImage(loadModel(),imagen)
        return render_template('result.html', prediccion=prediccion)


