import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

a = np.zeros((3,4))
print(a)

s = pd.Series([3,6,4,7])
print(s)

plt.plot(s)
plt.show()

img = cv2.imread("images/a_image.jpg")
cv2.imshow("leon",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
