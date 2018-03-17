import cv2
# read the relevant cascade using cv2.CascadeClassifier - used for face searching in an image
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# loading an image - can be dynamically for futural usages
img = cv2.imread("news.jpg")
# gray version of the same image - high accuracy when searching for a face inside it
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# detecMultiScale - search for cascade classifier and it return the coordinates for the face in an img (receives a rectangle)
faces = face_cascade.detectMultiScale(gray_img,
scaleFactor=1.1,
minNeighbors=5)
# scaleFactor - **smaller value - higher accuracy** - decreases the img, makes the faces bigger (search iteratively again and again for bigger faces)
# minNeighbors - how many Neighbors to search around the window (face window)
# print(type(faces))
# print(faces)

for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),3)
    #params - 1 - img that a rectangle will be drawn on.
    #2 - x,y - starting point
    #3 - where to end
    #4 - rectangle color by BGR (Blue, *Green*, Red)
    #5 - rectangle width


resized = cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)))
#resizing the img by: image, img.shape / 3, img.shape / 3 (w, h)
cv2.imshow("imgWithRectangleOnFace", resized)
# press any key and it closes the window
cv2.waitKey(0)
# destroy windows
cv2.destroyAllWindows()
