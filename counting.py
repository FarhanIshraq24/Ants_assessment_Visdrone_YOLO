from ultralytics import YOLO
import cv2

model = YOLO("/Users/farhanishraq/runs/detect/runs/detect/visdrone_yolov8-5/weights/best.pt")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, conf=0.25)[0]   # FIX: confidence threshold

    persons = 0
    cars = 0

    for box in results.boxes:
        cls = int(box.cls[0])

        if cls == 0:
            persons += 1
        elif cls == 1:
            cars += 1

    annotated = results.plot()

    cv2.putText(annotated, f"Persons: {persons}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.putText(annotated, f"Cars: {cars}", (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Counting", annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()