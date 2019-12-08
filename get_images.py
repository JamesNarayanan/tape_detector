import cv2
vidcap = cv2.VideoCapture('TapeVideo.mov')
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite("images/" + str(count) + ".jpg", image)     # save frame as JPG file
        print("Wrote image " + str(count))
    return hasFrames
sec = 0
frameRate = .1 #//it will capture image in each 0.1 second
count = 1
success = getFrame(sec)
while success:
    count += 1
    sec += frameRate
    success = getFrame(sec)