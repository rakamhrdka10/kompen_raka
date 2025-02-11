from pathlib import Path
import streamlit as st
from dotenv import load_dotenv
import os

import config
from utils import load_model, infer_uploaded_webcam

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
authorize_url = os.getenv("AUTHORIZE_URL")
redirect_url = os.getenv("REDIRECT_URL")

# Set up page configuration
st.set_page_config(
    page_title="EmoSync App",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main page title
st.title("EmoSync")

st.sidebar.header("DL Model Configuration")

# Model type set to "best.pt"
model_type = "best.pt"

confidence = float(st.sidebar.slider(
    "Select Model Confidence", 1, 100, 50)) / 100

# Path to the model
model_path = Path(config.DETECTION_MODEL_DIR, model_type)

# Load the trained model
try:
    model = load_model(model_path)
except Exception as e:
    st.error(f"Failed to load the model. Please check the specified path: {model_path}")
    st.stop()

# Configuration for Webcam source
# st.sidebar.header("Webcam Configuration")
source_selectbox = "Webcam"  # Only Webcam option

if source_selectbox == "Webcam":
    infer_uploaded_webcam(confidence, model)
else:
    st.error("Webcam source not selected.")
    st.stop()  # Stop execution if the webcam source is not selected
