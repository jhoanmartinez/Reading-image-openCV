import cv2

img =cv2.imread ("images/a_image.jpg")

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Split channels
blue, green, red = cv2.split(img)

cv2.imshow("Blue", blue)
cv2.waitKey(0)
#cv2.destroyAllWindows()

cv2.imshow("Green", green)
cv2.waitKey(0)
#cv2.destroyAllWindows()

cv2.imshow("Red", red)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Writing images
cv2.imwrite("writed_images/Blue.png",blue)
cv2.imwrite("writed_images/Green.png",green)
cv2.imwrite("writed_images/Red.png",red)
