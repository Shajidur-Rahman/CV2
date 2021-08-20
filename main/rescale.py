import cv2


# works in every where
def rescale_frame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)


# only for live videos
# def change_res(weidth, height):
#     capture.set(3,weidth)
#     capture.set(4, height)


# captuer = cv2.VideoCapture("../resources/Videos/dog.mp4")
#
# while True:
#     _, frame = captuer.read()
#
#     frame_resized = rescale_frame(frame)
#
#     cv2.imshow("Frame", frame)
#     cv2.imshow("Resized frame", frame_resized)
#
#     if cv2.waitKey(1) == ord('q'):
#         break
#
#
# captuer.release()
# cv2.destroyWindow(winname='it')


cv2.waitKey(0)  # use it for wait

