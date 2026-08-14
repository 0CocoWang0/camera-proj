import cv2;
import time;
from pathlib import Path;

# connected to iphone camera
cap = cv2.VideoCapture(1)
saveTo = Path(__file__).parent/"captures"
while True:
    ret, frame = cap.read()
    #ret = return value. did this operation actually work? 
    if not ret:
        break
    cv2.imshow("frameeeeeeeeee plez", frame)
    
    # one waitkey call. opens the envolpe and take whatever is inside and trim it
    key = cv2.waitKey(1) & 0xFF
    # ord getting numeric value
    if key == ord('q'):
        print("pressed q")
        break
    elif key == ord(' '):
        print("pressed space bar")
        shot = cv2.imwrite(f"{saveTo/time.strftime("%Y-%m-%d-%H%M%S", time.localtime())}.png",frame)
        print(str(shot))
        
cap.release() # release the camera
cv2.destroyAllWindows() # destroy all windows