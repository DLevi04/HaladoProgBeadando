import cv2
import pandas as pd
import matplotlib.pyplot as plt
from ultralytics import YOLO

# 1. Modell betöltése (az előre betanított COCO modell ismeri ezeket az osztályokat)
model = YOLO("yolov8n.pt")  # 'yolov8n.pt' gyors, 'yolov8m.pt' pontosabb

# COCO osztályazonosítók:
# 0: person (gyalogos), 1: bicycle (kerékpár), 2: car (személyautó)
# (opcionálisan: 3: motorcycle, 5: bus, 7: truck is hozzávehető az autókhoz)
TARGET_CLASSES = {
    0: "Gyalogos",
    1: "Kerékpár",
    2: "Autó"
}

# 2. Videó megnyitása
video_path = "C:/Users/leven/Documents/TrafficVideo/Traffic.mp4"  # Cseréld ki a saját videód elérési útjára!
cap = cv2.VideoCapture(video_path)

fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
frame_count = 0

