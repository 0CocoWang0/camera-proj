import cv2;
import time;
from pathlib import Path;
import subprocess;

# connected to iphone camera
cap = cv2.VideoCapture(0)
saveTo = Path(__file__).parent/"captures1.0"
saveTo.mkdir(exist_ok=True)


while True:
    ret, frame = cap.read()
    #ret = return value. did this operation actually work? 
    if not ret:
        break
    
    sth = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("frameeeeeeeeee plez", frame)
    cv2.imshow("sth", sth)
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
    
        
cap.release() # release the camera
cv2.destroyAllWindows() # destroy all windows