from ultralytics import YOLO

model = YOLO("/Users/farhanishraq/runs/detect/train-2/weights/best.pt")

model.track(
    source="test.mp4",
    tracker="bytetrack.yaml",
    show=True
)