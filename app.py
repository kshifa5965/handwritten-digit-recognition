from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import os

app = Flask(__name__)

# Load trained model
model = load_model("model.h5")

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None

    if request.method == "POST":

        file = request.files["file"]

        if file:

            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)

            file.save(filepath)

            image = Image.open(filepath).convert("L")

            image = image.resize((28, 28))

            image = np.array(image)

            image = 255 - image

            image = image / 255.0

            image = image.reshape(1, 28, 28, 1)

            result = model.predict(image)

            prediction = np.argmax(result)

    return render_template(
        "index.html",
        prediction=prediction
    )


if __name__ == "__main__":
    app.run(debug=True)