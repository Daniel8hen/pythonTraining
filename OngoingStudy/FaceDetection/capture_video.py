import cv2, time

# number - capture video from camera
# path - "movie.mp4" for example - for a specific video file
video = cv2.VideoCapture(0)
# check = boolean, frame = numpy array
while True:
    check, frame = video.read()
    print(check)
    print(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # wait 3 seconds - not needed in the loop
    # time.sleep(3)
    cv2.imshow("Capturing - Gray", gray)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    # release camera
video.release()
cv2.destroyAllWindows()
