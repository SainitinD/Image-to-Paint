import pyautogui
import time
import matplotlib.pyplot as plt
import numpy as np
import AppOpener


#load the picture
image = plt.imread("haaland.png")

# Convert image from rgb to grayscale
image = np.dot(image[:,:,0:3], [0.2989, 0.5870, 0.1140])

# for i in range(100):
#     if i % 10 == 0:
#         plt.show()
#     cutoff = i/100
#     new_img = np.copy(image)
#     new_img[new_img < cutoff] = 0.0
#     new_img[new_img >= cutoff] = 1.0
#     plt.subplot(1, 10, i%10+1)
#     plt.imshow(new_img, cmap='gray')


# Modify pixels to make then 1.0 (White) or 0.0 (Black)
cutoff = 0.53
image[image < cutoff] = 0.0
image[image >= cutoff] = 1.0
print(image.shape)

# Debugging
plt.imshow(image, cmap='gray')
plt.show()


# Updated Open 'Paint' Application
AppOpener.open("Paint")
time.sleep(2)

# Draw the image
pyautogui.PAUSE = 0
startX, startY = 40,280
w, h = image.shape  # w = width, h = height
for i in range(w):
    for j in range(h):
        if image[i,j] == 0:
            pyautogui.click(startX+j, startY+i, button='left')
