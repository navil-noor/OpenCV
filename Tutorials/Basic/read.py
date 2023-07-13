import cv2 as cv

# Reading image
img = cv.imread('Photos/bird1.jpg')
cv.imshow('Bird', img)

cv.waitKey(0)

# Reading Video
# capture = cv.VideoCapture('../Videos/Sunset.mp4')

# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('Video', frame)
#
#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break
#
# capture.release()
# cv.destroyAllWindows()
