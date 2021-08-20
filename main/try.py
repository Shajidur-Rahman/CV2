import cv2

img = cv2.imread("../resources/Photos/cat.jpg")
cv2.imshow("img", img)

def rescale_frame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)


resized = rescale_frame(img)
cv2.imshow("resized image", resized)

cv2.waitKey(0)  # use it for wait

