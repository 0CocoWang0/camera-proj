import cv2;


cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    #ret = return value. did this operation actually work? 
    if not ret:
        break
    cv2.imshow("frameeeeeeeeee plez", frame)
    
    # press q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'): # 0xff and ord are used together to look for a specific key press
        break 
    # if no 1 inside waitKey, it will wait indefinitely until a key is pressed -> freeze the vid on the very first frame
    
cap.release() # release the camera
cv2.destroyAllWindows() # destroy all windows