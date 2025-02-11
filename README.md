# Emotion Detection with YOLOv8

## Link Colab Training
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1AuZXEqys2IA5jk6ngWURG4R0V6nYHSH_?usp=sharing#scrollTo=CgH6OHHwO4pA)

## Requirements
```bash
streamlit==1.28.0
ultralytics==8.0.202
python-dotenv
requests
opencv-python==4.8.1.78
opencv-python-headless==4.8.1.78
Pillow==10.1.0
```
## how to run
1. Clone repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3.Jalankan aplikasi Streamlit:
```bash
streamlit run app.py
```
4. akses melalui :
- Local URL: http://localhost:8501
- Network URL: http://172.20.10.4:8501

## Dokumentasi Training
1. Persiapan GPU
2. Setup environment
3. Install library Ultralytics
4. Download dataset dari Roboflow
5. Training model dengan konfigurasi:
   - Epochs: 25 (sesuaikan)
   - Image size: 600x600
6. Model architecture: yolov8s
7. Validasi model
8. Testing dan prediksi
