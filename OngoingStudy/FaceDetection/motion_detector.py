import cv2, time

first_frame=None
# number - capture video from camera
# path - "movie.mp4" for example - for a specific video file
video = cv2.VideoCapture(0)
# check = boolean, frame = numpy array
while True:
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # The GaussianBlur removes noise and increases accuracy (used in photoshop as well)
    gray = cv2.GaussianBlur(gray, (21,21), 0)

    # happens only in the 1st iteration of course
    if first_frame is None:
        #gray in 1st iteration is the gray ver. of the video
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame,gray)

    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    # > 30 - assign white (255), otherwise it'll be 0. last argument - treshold method (binary - 1 /0)
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)
    #dilation

    (_,cnts,_)=cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for countour in cnts:
        if cv2.contourArea(countour) < 1000: #pixels
            continue
        # else - draw rectangle (since there's motion)
        (x, y, w, h) = cv2.boundingRect(countour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    cv2.imshow("Gray Frame", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frmae", thresh_frame)
    cv2.imshow("Color Frame", frame)

    key = cv2.waitKey(1)
    print(gray)
    print(delta_frame)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
