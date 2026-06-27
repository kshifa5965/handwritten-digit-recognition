# Handwritten Digit Recognition Using CNN

## Project Overview

This project is a web-based Handwritten Digit Recognition System developed using Python, TensorFlow, Keras, Flask, HTML, CSS, and JavaScript. It uses a Convolutional Neural Network (CNN) trained on the MNIST dataset to recognize handwritten digits from uploaded images.

---

## Features

- Handwritten digit recognition (0–9)
- CNN model trained on the MNIST dataset
- Flask backend
- User-friendly web interface
- Image upload functionality
- Real-time prediction
- Responsive design

---

## Technologies Used

- Python
- TensorFlow
- Keras
- Flask
- HTML5
- CSS3
- JavaScript
- NumPy
- Pillow (PIL)

---

## Project Structure

```
Handwritten-Digit-Recognition/
│
├── app.py
├── train.py
├── model.h5
├── uploads/
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/Handwritten-Digit-Recognition.git
```

### Open the Project Folder

```bash
cd Handwritten-Digit-Recognition
```

### Install Dependencies

```bash
pip install flask tensorflow pillow numpy matplotlib
```

---

## Train the Model

Run:

```bash
python train.py
```

The trained model will be saved as:

```
model.h5
```

---

## Run the Application

Start the Flask server:

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## Usage

1. Open the application in your browser.
2. Click **Choose File**.
3. Select a handwritten digit image.
4. Click **Predict Digit**.
5. View the predicted result.

---

## CNN Architecture

- Conv2D (32 Filters)
- MaxPooling2D<img width="442" height="429" alt="7" src="https://github.com/user-attachments/assets/7c9ed3a3-3b86-426b-a0c6-4b1cb1902748" />

- Conv2D (64 Filters)
- MaxPooling2D
- Flatten
- Dense (128 Neurons)
- Dense (10 Output Classes)

---

## Dataset

- Dataset: MNIST
- Training Images: 60,000
- Testing Images: 10,000
- Image Size: 28 × 28 pixels
- Classes: Digits 0–9

---

## Expected Accuracy

Approximately **98–99%** on the MNIST test dataset.

---

## Future Enhancements

- Draw digits directly on the webpage
- Display prediction confidence
- Support multiple image uploads
- Deploy to the cloud
- Mobile-friendly interface

---

## Author

**K Shifa**

Internship Project

---

## License

This project is developed for educational and internship purposes only.<img width="442" height="429" alt="7" src="https://github.com/user-attachments/assets/1409cb58-c25e-4543-ac18-2aa8962dfeb4" />
<img width="442" height="429" alt="7" src="https://github.com/user-attachments/assets/c05be31d-ba90-4a97-9b00-57ed89f261e8" />
