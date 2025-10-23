# 😀 Emoji Face Detector

![Python](https://img.shields.io/badge/Python-3.10+-blue) 
![OpenCV](https://img.shields.io/badge/OpenCV-4.12.0-lightgrey) 
![DeepFace](https://img.shields.io/badge/DeepFace-0.0.95-orange) 
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.20.0-red) 

A **real-time emoji face detector** using Python, OpenCV, and DeepFace. This project detects your facial expressions from your webcam and overlays the corresponding emoji on your face in real-time.

---

## 🎯 Features

- Real-time emotion detection from webcam feed  
- Supports multiple emotions: **Happy**, **Sad**, **Angry**, **Surprise**  
- Uses **DeepFace** for facial analysis  
- Lightweight and easy to run  
- Can be extended to more emotions  

---

## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/emoji-face-detector.git
cd emoji-face-detector

# On Windows
python -m venv .venv
.venv\Scripts\Activate.ps1

# On Mac/Linux
python -m venv .venv
source .venv/bin/activate

---
##Install Dependencies

pip install -r requirements.txt

##PROJECT STRUCTURE

emoji-face-detector/
│
├── app.py                # Main Python script
├── emojis/               # Folder with emoji images
│   ├── happy.png
│   ├── sad.png
│   ├── angry.png
│   └── surprise.png
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

python app.py

