# 🚁 VisDrone Object Detection, Counting & Tracking (YOLOv8)

This project is developed as part of the ANTS AI Assessment. It focuses on **object detection, human counting, and optional object tracking** using the VisDrone dataset with YOLOv8.

---

## 📌 Project Overview

The goal of this project is to:
- Detect **humans (persons)** and **vehicles (cars)** in aerial drone images/videos
- Perform **real-time human counting**
- (Optional) Apply **object tracking for continuous identification**
- Evaluate model performance on a real-world drone dataset

---

## 📂 Dataset

We use the **VisDrone 2019 Object Detection Dataset**:

- Source: https://www.kaggle.com/datasets/banuprasadb/visdrone-dataset
- Contains aerial images captured from drones
- Highly dense scenes with:
  - pedestrians
  - vehicles
  - occlusions
  - small objects

### 🔄 Classes used in this project:
| Original Class | Mapped Class |
|----------------|-------------|
| Pedestrian     | Person (0)  |
| People         | Person (0)  |
| Car            | Car (1)     |
| Van/Truck/Bus  | Car (1)     |

Only **2 classes** are used for simplified detection.

---

## ⚙️ Installation

```bash
pip install ultralytics opencv-python numpy matplotlib