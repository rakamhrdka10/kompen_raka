from ultralytics import YOLO
import streamlit as st
import cv2
from PIL import Image
import tempfile

@st.cache_resource
def load_model(model_path):
    model = YOLO(model_path)
    return model

def _display_detected_frames(conf, model, st_frame, image, result=None):
    if result is None:
        # Jika result tidak disediakan, lakukan inferensi
        result = model.predict(image, conf=conf)[0]

    # Ekstrak label emosi dari hasil deteksi
    cls = result.boxes.cls
    label = "Unknown"

    if len(cls) > 0:
        # Diasumsikan menggunakan nilai kelas dari kotak pertama jika terdapat beberapa kotak
        label_idx = int(cls[0])
        names = result.names
        label = names[label_idx]

    res_plotted = result.plot()
    st_frame.image(res_plotted,
                   caption='Video Terdeteksi',
                   channels="BGR",
                   use_column_width=True
                   )

    return label


def handle_emotion(emotion):
    # Mendefinisikan tautan Spotify untuk setiap emosi
    spotify_links = {
        "Angry": "https://open.spotify.com/playlist/37i9dQZF1EIgNZCaOGb0Mi",
        "Sad" : "https://open.spotify.com/genre/0JQ5DAqbMKFGTIdqXPDTSL",
        "Neutral": "https://open.spotify.com/genre/0JQ5DAqbMKFFzDl7qN9Apr",
        "Happy": "https://open.spotify.com/genre/0JQ5IMCbQBLtqe3T85WC6v",
        "Disguist": "https://open.spotify.com/playlist/5sBr8wixKxPk6FQuCxyq32",
        "Surprise": "https://open.spotify.com/playlist/3CUpYjEl8N4KQWT57iJJD7"
    }

    # Memeriksa apakah emosi ada dalam daftar
    if emotion in spotify_links:
        spotify_link = spotify_links[emotion]
        st.markdown(f"[Click here to open Spotify]({spotify_link})", unsafe_allow_html=True)
    else:
        st.write("No emotion detected or emotion not recognized.")

def infer_uploaded_webcam(conf, model):
    try:
        capture_button = st.button(label="Capture Image")
        stop_button = st.button(label="Stop")

        vid_cap = cv2.VideoCapture(0)
        st_frame = st.empty()
        last_detected_emotion = "Unknown"

        while not stop_button:
            success, image = vid_cap.read()

            if success:
                last_detected_emotion = _display_detected_frames(conf, model, st_frame, image)

                # Check if "Capture Image" button is pressed
                if capture_button:
                    capture_button = False  # Reset the button state after capturing
                    st.write(f"Last detected expression: {last_detected_emotion}")
                    handle_emotion(last_detected_emotion)

            else:
                vid_cap.release()
                break
    except Exception as e:
        st.error(f"Video loading error: {str(e)}")

    return last_detected_emotion


