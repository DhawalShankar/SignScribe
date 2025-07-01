import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase # type: ignore
import cv2
import mediapipe as mp
import numpy as np
import joblib

# Streamlit UI setup
st.set_page_config(page_title="SignScribe", layout="centered")
st.title("🤟 SignScribe: Gesture to Text Translator")

# Load the trained model
model = joblib.load("models/gesture_model.pkl")

# Mediapipe Hands setup
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Define the transformer class
class HandGestureTransformer(VideoTransformerBase):
    def __init__(self):
        self.hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        img = cv2.flip(img, 1)
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = self.hands.process(rgb)

        prediction = "..."

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                try:
                    data = []
                    for lm in hand_landmarks.landmark:
                        data.extend([lm.x, lm.y, lm.z])
                    prediction = model.predict([data])[0]
                except Exception:
                    prediction = "❌ Prediction Failed"

        # Show prediction below webcam (optional but cool)
        cv2.putText(img, f'Gesture: {prediction}', (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        return img

# Start the webcam stream
webrtc_streamer(
    key="signscribe",
    video_transformer_factory=HandGestureTransformer,
    media_stream_constraints={"video": True, "audio": False},
    async_processing=True
)
