import cv2
import json
from keras.models import model_from_json
import numpy as np
from tensorflow.keras.models import model_from_json
import json
import keras

def load_reshape_image(path):
    #cambiar tamaño imagen
    image = cv2.imread(path)
    if image.shape != (224,224,3):
        image = cv2.resize(image, (224,224))
    image = image.reshape(1,224,224,3)
    return image

def loadModel():
    #cargar el modelo
    with open('src/model_CNN_definitivo.json','r') as f:
        model_json = json.load(f)
    loaded_model = model_from_json(model_json)
    loaded_model.load_weights("src/Checkpoint_CNN_02_0.61")
    #print("Loaded model from disk")
    return loaded_model


def predictNewImage(model,image):
    model.compile(loss=keras.losses.categorical_crossentropy, optimizer='adam', metrics=['accuracy'])
    prediccion = model.predict(image)
    predicIndex = np.argmax(prediccion, axis=1)
    if predicIndex == 0:
        return "This gastrointestinal tumor has been classified as a MSI tumor. The patient may respond to immunotherapy."
    else:
        return "This gastrointestinal tumor has been classified as a MSS tumor. Immunotherapy treatment is not recommended."