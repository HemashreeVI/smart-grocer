import cv2

image_path = "data/test_images/test.jpg"

image = cv2.imread(image_path)

if image is None:
    print("Could not load the image.")
    exit()

height, width, channels = image.shape

print("Image loaded successfully!")
print(f"Width: {width}")
print(f"Height: {height}")
print(f"Channels: {channels}")

cv2.imwrite("data/test_images/test_copy.jpg", image)

print("Image copy created successfully.")