import cv2;
import time;
from pathlib import Path;
import subprocess;
import numpy as np;


# connected to iphone camera
cap = cv2.VideoCapture(0)
saveTo = Path(__file__).parent/"captures1.0"
saveTo.mkdir(exist_ok=True)

# a green highlighter
# (H - which colour, S - how vivid, V - how bright)
lowc = np.array([35, 80, 80])
highc = np.array([85, 255, 255])


while True:
    ret, frame = cap.read()
    #ret = return value. did this operation actually work? 
    if not ret:
        break
    
    sth = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    sth2 = cv2.inRange(sth, lowc, highc)
    cv2.circle(frame, (sth.shape[1]//2, sth.shape[0]//2), 100, (0, 0, 255), 2)
    cv2.imshow("frameeeeeeeeee plez", frame)
    cv2.imshow("sth", sth)
    cv2.imshow("again sth", sth2)
    
    # one waitkey call. opens the envolpe and take whatever is inside and trim it
    key = cv2.waitKey(1) & 0xFF
    # ord getting numeric value
    if key == ord('q'):
        subprocess.Popen(["afplay", "/System/Library/Sounds/Hero.aiff"])
        print("pressed q")
        break
    elif key == ord(' '):
        subprocess.Popen(["afplay", "/System/Library/Sounds/Purr.aiff"])
        print("pressed space bar")
        shot = cv2.imwrite(saveTo / f"{time.strftime("%Y-%m-%d-%H%M%S", time.localtime())}.png",frame)
        shot2 = cv2.imwrite(saveTo / f"{time.strftime("%Y-%m%d-%H%M%S", time.localtime())} special.png", sth)
        print(str(shot), str(shot2))
        
    elif key == ord('h'):
        # shape[0] is height, shape[1] is width. // keeps index an integer
        print(sth[sth.shape[0]//2, sth.shape[1]//2])
    
        
cap.release() # release the camera
cv2.destroyAllWindows() # destroy all windows