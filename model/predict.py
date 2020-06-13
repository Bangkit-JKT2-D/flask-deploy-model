import tensorflow as tf
import base64
import io
import numpy as np
from PIL import Image
from keras.preprocessing import image

model = tf.keras.models.load_model('model/model.h5')
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

def preprocess_image(img, target_size):
    if img.mode != "RGB":
        img = img.convert("RGB")
    img = img.resize(target_size)
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    return img

def predict(data):
    img = Image.open(data)
    processed_image = preprocess_image(img, target_size=(150, 150))

    images = np.vstack([processed_image])
    classes = model.predict(images, batch_size=10)
    max = np.amax(classes[0])
    if np.where(classes[0] == max)[0] == 0:
        return 'Fresh Apple'
    elif np.where(classes[0] == max)[0] == 1:
        return 'Fresh Banana'
    elif np.where(classes[0] == max)[0] == 2:
        return 'Fresh Orange'
    elif np.where(classes[0] == max)[0] == 3:
        return 'Rotten Apple'
    elif np.where(classes[0] == max)[0] == 4:
        return 'Rotten Banana'
    else:
        return 'Rotten orange'