from ultralytics import YOLO

def main():
    model = YOLO("yolov8n.pt")

    model.train(
        data="visdrone.yaml",
        epochs=10,
        imgsz=640,
        batch=8,
        device="mps",
        project="runs/detect",
        name="visdrone_yolov8",
        patience=20
    )

if __name__ == "__main__":
    main()