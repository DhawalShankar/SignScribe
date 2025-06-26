# 🤟 SignScribe - A Gesture to Text Translator 

A unique real-time gesture-to-text translation system built using MediaPipe, OpenCV, and scikit-learn. This project lets you collect your own hand gesture data, train a machine learning model, and use it to recognize gestures and convert them into text — **your own data, your own gestures, your own model**.

---

## ✨ Features

- 🎥 Real-time webcam gesture tracking using MediaPipe
- 🖐️ Collect multiple gesture datasets with custom labels
- 🧠 Train a Random Forest Classifier on your personalized data
- 📖 Predict gestures in real time and convert to text
- 🪶 Fully Pythonic, minimal dependencies, no deep learning

---

## 📁 Project Structure

```

gesture-to-text/
├── collect\_data.py          # For collecting gesture samples
├── train\_model.py           # For training ML model
├── predict.py               # For real-time prediction
├── data/                    # Folder where gesture .npy data is saved
├── model.pkl                # Trained model file (auto-generated)
├── requirements.txt         # All required libraries
├── .gitignore               # Files/folders to ignore in git
├── LICENSE                  # MIT License
└── README.md                # You're reading this!

````

---

## 🔧 Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/gesture-to-text.git
cd gesture-to-text
````

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

---

## 🎯 Usage

### Step 1: Collect Gesture Data

```bash
python3 collect_data.py
```

👉 You will be prompted to enter a gesture name.
✌️ Show your gesture clearly in the webcam window.
📦 100 samples per gesture are saved as `.npy` files inside `data/`.

> ℹ️ Run this script separately for each gesture you want to train on.

---

### Step 2: Train the Model

```bash
python3 train_model.py
```

📚 This trains a Random Forest model on your collected data
💾 Model is saved automatically as `model.pkl`

---

### Step 3: Predict in Real Time

```bash
python3 predict.py
```

🧠 Model loads and starts webcam
🖐️ Show your trained gesture — it will print the predicted gesture name

---

## 📦 Requirements

```txt
mediapipe
opencv-python
scikit-learn
numpy
pandas
matplotlib
```

All installed via:

```bash
pip install -r requirements.txt
```

---

## 🔒 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙏 Credits

Made with 💙 by [Dhawal Shankar](https://github.com/dhawalshankar),
ECE + CS enthusiast and a devoted learner of Bharatiya values.

> **"श्रम और सत्य से बना शोध कभी व्यर्थ नहीं जाता।"**

---

## 💡 Future Ideas

* Add Text-to-Speech (gTTS or pyttsx3)
* Add GUI with Streamlit or Tkinter
* Export results as subtitles
* Use time-series models for dynamic gestures

````


