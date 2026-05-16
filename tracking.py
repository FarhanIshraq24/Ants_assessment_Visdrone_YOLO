from ultralytics import YOLO

model = YOLO("/Users/farhanishraq/runs/detect/runs/detect/visdrone_yolov8-5/weights/best.pt")

results = model.track(
    source="test.mp4",
    tracker="bytetrack.yaml",
    save=True,
    conf=0.25,
    persist=True
)

print("Tracking complete → check runs/detect/")