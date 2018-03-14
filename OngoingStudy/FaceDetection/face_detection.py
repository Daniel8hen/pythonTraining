import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("photo.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img,
#smaller value - higher accuracy - decreases the img, makes the faces bigger
scaleFactor=1.1,
# how many Neighbors to search around the window (face window)
minNeighbors=5)

print(type(faces))
print(faces)

for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),3)
    #params - 1 - img that a rectangle will be drawn on.
    #2 - x,y - where to start.
    #3 - where to end
    #4 - rectangle color by BGR
    #5 - line width

resized = cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)))
#Gray version of the image
cv2.imshow("imgWithRectangleOnFace", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
