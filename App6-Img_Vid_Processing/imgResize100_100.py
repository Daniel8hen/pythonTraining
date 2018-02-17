import cv2
import glob
#script that gets a list of images in a dir and resizes them to 100x100
# running on the list using glob (unix style pathname pattern expansion) - find path name by file name
heightAndWidth = 100
img_list = glob.glob("*.jpg")
for img in img_list:
    #read the image
    image_to_resize = cv2.imread(img, 0)
    #resize the image to relevant h, w
    resized_image = cv2.resize(image_to_resize, (heightAndWidth, heightAndWidth))
    cv2.imshow("Hey",resized_image)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+img,resized_image)
