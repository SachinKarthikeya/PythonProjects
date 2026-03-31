import cv2

image = cv2.imread('ed37cfce-de68-45f5-a225-62021e85bc85.JPG', cv2.IMREAD_UNCHANGED)

scale_percent = 50

width = int(image.shape[1] * scale_percent/100)
height = int(image.shape[0] * scale_percent/100)

new_size = (width, height)

output = cv2.resize(image, new_size)

cv2.imwrite('resized_image.jpg', output)
cv2.waitKey(0)