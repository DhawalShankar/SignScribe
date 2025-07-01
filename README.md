# 🤟 SignScribe - A Gesture to Text Translator 

A unique real-time gesture-to-text translation system built using MediaPipe, OpenCV, and scikit-learn. This project lets you collect your own hand gesture data, train a machine learning model, and use it to recognize gestures and convert them into text — **your own data, your own gestures, your own model**.

Now also includes a clean **Streamlit-based web interface** (`app.py`) for live gesture prediction. *(Not deployed yet, but locally runnable.)*

---

## ✨ Features

- 🎥 Real-time webcam gesture tracking using MediaPipe
- 🖐️ Collect custom gesture datasets with labels
- 🧠 Train a Random Forest Classifier on your personalized gestures
- 📖 Predict gestures in real-time and convert to text
- 💻 Now includes an interactive **Streamlit GUI** for gesture prediction
- 🪶 Fully Pythonic, minimal dependencies, no deep learning

---

## 📁 Project Structure

```

gesture-to-text/
├── app.py                   # NEW: Streamlit UI for live prediction
├── collect\_data.py          # For collecting gesture samples
├── train\_model.py           # For training ML model
├── predict.py               # For terminal-based real-time prediction
├── data/                    # Folder for gesture .npy data
├── models/
│   └── gesture\_model.pkl    # Trained model (auto-generated)
├── requirements.txt         # Python dependencies
├── .gitignore               # Files to ignore in git
├── LICENSE                  # MIT License
└── README.md                # You're reading this!

````

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/dhawalshankar/gesture-to-text.git
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

## 🎯 Usage Guide

### 🔹 Step 1: Collect Gesture Data

```bash
python3 collect_data.py
```

* You'll be prompted for gesture name.
* Show your gesture clearly on the webcam.
* 100 samples per gesture will be saved in `data/`.

### 🔹 Step 2: Train the Model

```bash
python3 train_model.py
```

* Trains a Random Forest classifier using collected gestures
* Saves model as `models/gesture_model.pkl`

### 🔹 Step 3: Predict Gestures

#### a. Terminal-Based (CLI)

```bash
python3 predict.py
```

#### b. Streamlit App (GUI)

```bash
streamlit run app.py
```

> *(Note: This version is not yet deployed on the cloud, but runs locally.)*

---

## 📦 Requirements

```
streamlit
mediapipe
opencv-python
scikit-learn
numpy
joblib
```

Install with:

```bash
pip install -r requirements.txt
```

---

## 💡 Future Roadmap

* 🎙️ Add text-to-speech feedback (gTTS or pyttsx3)
* 📝 Save gesture logs as subtitle files
* 🔄 Explore time-series models for dynamic gestures
* 🌐 Deploy Streamlit app on Vercel/HF/Streamlit Cloud

---

## 🙏 Credits

Made with 💙 by [Dhawal](https://github.com/dhawalshankar),



