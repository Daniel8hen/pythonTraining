import cv2, time, pandas
from datetime import datetime

first_frame=None
status_list = [None, None]
times = []
df = pandas.DataFrame(columns=["Start","End"])
# number - capture video from camera
# path - "movie.mp4" for example - for a specific video file
video = cv2.VideoCapture(0)
# check = boolean, frame = numpy array
while True:
    check, frame = video.read()
    status = 0
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
        if cv2.contourArea(countour) < 10000: #pixels
            continue
        status = 1
        # else - draw rectangle (since there's motion)
        (x, y, w, h) = cv2.boundingRect(countour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    status_list.append(status)
    # statusDelta - using last two items in the list
    if status_list[-1]==1 and status_list[-2]==0: # the 1 before is 1, the 1 before it is 0
        times.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1: # the 1 before is 1, the 1 before it is 0
        times.append(datetime.now())
    cv2.imshow("Gray Frame", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frmae", thresh_frame)
    cv2.imshow("Color Frame", frame)

    key = cv2.waitKey(1)
    # print(gray)
    # print(delta_frame)

    if key == ord('q'):
        if status == 1:
            times.append(datetime.now())
        break

print(status_list)
print(times)
# iterate through times list
for i in range(0, len(times), 2):
    df = df.append({"Start": times[i], "End":times[i+1]}, ignore_index=True)

df.to_csv("MotionData.csv")

video.release()
cv2.destroyAllWindows()
