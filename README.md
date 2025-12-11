# Face Emotion Analyzer  
### Real-Time Emotion Detection using Mediapipe + DeepFace + Flask + JavaScript

This project is a complete real-time facial emotion recognition system built using **DeepFace**, **Mediapipe**, **Flask**, and a lightweight **HTML/CSS/JavaScript** frontend.

It captures a frame from the user’s webcam, sends it to a Python backend, and returns:

- Detected faces  
- Bounding boxes  
- Dominant emotion  
- Emotion confidence  

All **7 emotions** supported by DeepFace are analyzed:
**happy, sad, angry, disgust, fear, surprise, neutral**.

A modern UI displays these results along with live bounding-box overlays.

---

## 🔥 Features

- 🎥 **Webcam Capture**  
- 🧠 **DeepFace Emotion Recognition**  
- 👁️ **Mediapipe Face Detection** (via backend)  
- 🟩 **Bounding Box Overlay** on video preview  
- 🚀 **REST API (Flask)**  
- 🌐 **Frontend Dashboard with Real-Time Rendering**  
- 👍 Supports **multiple faces**  

---

## 🧠 Tech Stack

| Component | Technology |
|----------|------------|
| Backend | Python, Flask |
| Emotion Model | DeepFace |
| Detector | Mediapipe |
| Image Processing | OpenCV |
| Frontend | HTML, CSS, JavaScript |
| Communication | REST (JSON) |

---

## 📁 Project Structure

project-folder/
│
├── app.py # Backend (Flask + DeepFace + Mediapipe)
├── index.html # Frontend dashboard with webcam UI
├── README.md # Documentation
└── requirements.txt # Optional dependency list

yaml
Copy code

---

## ⚙️ Installation

### 1️⃣ Install dependencies

```bash
pip install flask flask-cors deepface mediapipe numpy opencv-python
2️⃣ Start backend server
bash
Copy code
python app.py
Backend runs at:

cpp
Copy code
http://127.0.0.1:8000
Test:

arduino
Copy code
http://127.0.0.1:8000/ping
3️⃣ Start frontend
bash
Copy code
python -m http.server 8080
Open:

arduino
Copy code
http://127.0.0.1:8080/index.html
🖥️ Usage
Click Start Camera

Position your face in the frame

Click Analyze Frame

View:

Detected faces

Bounding boxes

Emotion prediction

Confidence percentage

📡 API Endpoint
POST /analyze
Example response:

json
Copy code
{
  "faces": [
    {
      "emotion": "happy",
      "confidence": 0.91,
      "bbox": { "xmin": 120, "ymin": 80, "xmax": 240, "ymax": 260 }
    }
  ],
  "num_faces": 1,
  "frame_width": 640,
  "frame_height": 480
}
🧬 Emotions Detected
DeepFace supports prediction for:

Angry

Disgust

Fear

Happy

Sad

Surprise

Neutral

The highest-confidence emotion is returned as the dominant prediction.

🚀 Future Enhancements
Continuous real-time streaming (instead of single-frame analysis)

ONNX-optimized emotion model for higher FPS

Add age, gender, and face ID recognition

Deploy backend to cloud (Render, AWS, Railway)

Host frontend on Netlify/Vercel

🤝 Contributing
Contributions are welcome.
Open an issue for feature requests or improvements.

📜 License
MIT License.

👤 Author
Vignesh
AI/ML Developer | Computer Vision | Deep Learning
