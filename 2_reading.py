import cv2

# Load image
img = cv2.imread("images/a_image.jpg")

if img is None:
    print("Imagen no encontrada")

# Display image
cv2.imshow("Imagen", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
