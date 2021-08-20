import cv2  # import cv2

# reading images
# img = cv2.imread("../resources/Photos/cat.jpg")  # reading
# cv2.imshow("Cat", img)  # showing image

# reading videos
# captuer = cv2.VideoCapture("../resources/Videos/dog.mp4")
captuer = cv2.VideoCapture("../resources/Videos/dog.mp4")

while True:
    _, frame = captuer.read()
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) == ord('q'):
        break


captuer.release()
cv2.destroyWindow(winname='it')
cv2.waitKey(0)  # use it for wait
