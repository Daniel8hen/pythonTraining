import cv2, time

first_frame=None
# number - capture video from camera
# path - "movie.mp4" for example - for a specific video file
video = cv2.VideoCapture(0)
# check = boolean, frame = numpy array
while True:
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # below removes noise and increases accuracy
    gray = cv2.GaussianBlur(gray, (21,21), 0)

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame,gray)

    thresh_delta = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]

    cv2.imshow("Gray Frame", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frmae", thresh_delta)

    key = cv2.waitKey(1)
    print(gray)
    print(delta_frame)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
