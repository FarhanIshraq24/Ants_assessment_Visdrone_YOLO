# 🚀 Smart Traffic Surveillance using YOLOv8 + ByteTrack

## 📌 Project Overview
This project implements a real-time object detection and tracking system using YOLOv8 trained on the VisDrone dataset. The system detects and counts **humans and vehicles** in real-time video streams using deep learning and multi-object tracking.

---

## ⚙️ Features
- YOLOv8-based object detection
- Custom training on VisDrone dataset
- Human & vehicle detection (2-class model)
- ByteTrack-based multi-object tracking
- Unique object counting (ID-based)
- Real-time webcam & video inference
- Annotated output video generation

---

## 🧠 Model Architecture
- Base Model: YOLOv8n
- Tracker: ByteTrack
- Framework: Ultralytics
- Input size: 640x640
- Classes: Person, Car

---

## 📂 Dataset
VisDrone Dataset (converted to YOLO format)
- Person → class 0
- Car → class 1

---

## 🚀 Training
```bash
python train.py