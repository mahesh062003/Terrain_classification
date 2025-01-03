from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from io import BytesIO

app = Flask(__name__)

# Load the pre-trained model
model = load_model('model.h5')  # Replace with the path to your saved model file

# Mapping of class indices to class names
class_names = {0: 'grassy', 1: 'marshy', 2: 'rocky', 3: 'sandy'}  # Update with your class names

# Define a route for the main page
@app.route('/')
def index():
    return render_template('index.html')

# Define a route for handling the image upload and making predictions
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']

    if file.filename == '':
        return "No selected file"

    # Load and preprocess the uploaded image
    img = image.load_img(BytesIO(file.read()), target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0  # Normalize the image data

    # Use the loaded model to predict the class of the uploaded image
    predictions = model.predict(img_array)

    # Get the predicted class label
    predicted_class_index = np.argmax(predictions)

    # Get the predicted class name
    predicted_class_name = class_names[predicted_class_index]

    # Render the template with the predicted class
    return render_template('index.html', predicted_class=predicted_class_name)

if __name__ == '__main__':
    app.run(debug=True)
