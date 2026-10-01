from ultralytics import YOLO

# Load pretrained YOLO model
model = YOLO("yolo11n.pt")

# Run detection
results = model("data/test_images/test.jpg")

# Save image with bounding boxes
for result in results:
    annotated_image = result.plot()
    result.save(filename="data/test_images/yolo_result.jpg")

    print("\nDetected objects:")

    for box in result.boxes:
        class_id = int(box.cls[0])
        confidence = float(box.conf[0])
        class_name = result.names[class_id]

        print(
            f"{class_name} - "
            f"confidence: {confidence:.2f}"
        )

print("\nAnnotated image saved successfully.")