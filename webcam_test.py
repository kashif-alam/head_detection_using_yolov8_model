from ultralytics import YOLO
import cv2

# Load your trained model (best.pt)
model = YOLO("best.pt")

# Open webcam (0 = default camera, change if you have multiple cams)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Run YOLOv8 inference
    results = model(frame)

    # Visualize results on the frame
    annotated_frame = results[0].plot()

    # Show the frame
    cv2.imshow("YOLOv8 Live Webcam", annotated_frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
