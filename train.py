from ultralytics import YOLO

def main():
    # Load pretrained YOLOv8 model
    model = YOLO("yolov8n.pt")  # start small for fast training

    # Train model
    results = model.train(
        data="datasets/VisDrone_Dataset/visdrone.yaml",  # your dataset config
        epochs=10,
        imgsz=416,
        batch=8,
        device="cpu",   # Apple Silicon (use "cuda" if NVIDIA GPU)
        workers=2,
        project="runs/detect",
        name="visdrone_yolov8",
        patience=20,
        cache=False
    )

    print("Training completed!")
    print(results)

if __name__ == "__main__":
    main()