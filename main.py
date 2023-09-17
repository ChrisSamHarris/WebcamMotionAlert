import cv2
# https://opencv.org/
# https://docs.opencv.org/4.x/d2/d96/tutorial_py_table_of_contents_imgproc.html
import time
from send_email import send_email
import glob

video = cv2.VideoCapture(0)
time.sleep(1)

first_frame = None
move_status_ls = []
count = 1

while True:
    move_status = 0
    
    check, frame = video.read()

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    if first_frame is None:
        first_frame = gray_frame_gau

    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)
    # cv2.imshow("My Video", delta_frame)

    thresh_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)
    cv2.imshow("My Video", dil_frame)

    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 3)
        if rectangle.any():
            move_status = 1
            cv2.imwrite(f"images/image_{count}.png", frame)
            count += 1
            all_images = glob.glob("images/*.png")
            image_index = int(len(all_images) / 2)
            image_to_send = all_images[image_index]

            
    move_status_ls.append(move_status)
    move_status_ls = move_status_ls[-2:]

    if move_status_ls[0] == 1 and move_status_ls[1] == 0:
        # This occurs once an object leaves the frame
        # [0,0] = No difference
        # [0,1] = object enters the frame
        # [1,1] = new object is still in the frame
        # [1,0] = Object has left the frame
        send_email()

    cv2.imshow("Video", frame)
    key = cv2.waitKey(1)

    if key == ord("q"):
        print("\n⚠️ Program Stopped through application\n")
        break

print(first_frame)
video.release()