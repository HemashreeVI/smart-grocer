import cv2

image_path = "data/test_images/test.jpg"

image = cv2.imread(image_path)

if image is None:
    print("Could not load the image.")
else:
    height, width, channels = image.shape

    print("Image loaded successfully!")
    print(f"Width: {width}")
    print(f"Height: {height}")
    print(f"Channels: {channels}")