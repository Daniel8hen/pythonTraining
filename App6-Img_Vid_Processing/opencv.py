import cv2
#2nd param:
# 1 - as it is (color)
# 0 - black and white
# -1 - transparency + color
img = cv2.imread("galaxy.jpg", 0)
print(img) #type = numpy on n dimension of array
print(img.shape) #wXh / RGB if it's 1
print(img.ndim) # num of dimensions

resized_image = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("Galaxy", resized_image)
cv2.imwrite("Galaxy_resized.jpg", resized_image)
cv2.waitKey(0) # 0 for keeping the img
cv2.destroyAllWindows()
