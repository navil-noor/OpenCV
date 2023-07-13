import cv2 as cv

# img = cv.imread('../Photos/bird1.jpg')
# cv.imshow('Bird', img)

# cv.waitKey(0)

def rescaleFrame(frame, scale=0.25):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# Reading Videos
capture = cv.VideoCapture('../Videos/Sunset.mp4')

while True:
    isTrue, frame = capture.read()

    if not isTrue:
        # Break the loop if there are no more frames to read
        break

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
