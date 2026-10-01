from ultralytics import YOLO

# Load a pretrained YOLO model
model = YOLO("yolo11n.pt")

# Run detection on our test image
results = model("data/test_images/test.jpg")

# Print detected objects
for result in results:
    print("\nDetected objects:")

    for box in result.boxes:
        class_id = int(box.cls[0])
        confidence = float(box.conf[0])
        class_name = result.names[class_id]

        print(
            f"{class_name} - "
            f"confidence: {confidence:.2f}"
        )