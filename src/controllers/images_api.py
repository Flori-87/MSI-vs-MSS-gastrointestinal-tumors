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
        # obtenemos el archivo del input "archivo"
        file = request.files['myFile']
        filename = secure_filename(file.filename)
        # Guardamos el archivo en el directorio "Archivos PDF"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Retornamos una respuesta satisfactoria con la predicción
        imagen = load_reshape_image(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        prediccion = predictNewImage(loadModel(),imagen)
        return render_template('result.html', prediccion=prediccion)
    """
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['myFile']
        print(file)
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        model = loadModel()
        imagen = load_reshape_image(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        prediccion = predictNewImage(model,imagen)
        return prediccion
        """

