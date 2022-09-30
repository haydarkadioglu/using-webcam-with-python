
import cv2 as cv

from datetime import datetime



# current date and time
now = datetime.now()
s1 = now.strftime("%m%d%Y_%H%M%S")


capp = cv.VideoCapture(0, cv.CAP_DSHOW)


filename = f"{s1}" + ".jpg"


while True:
    ret, frame = capp.read()
    frame = cv.flip(frame, 1)
      
        
    
            

    cv.imshow("HaydarCam// click 'q' for close the application", frame)

    if cv.waitKey(30) & 0xFF == ord("q") or 0xFF == ord("Q"):
        cv.imwrite(filename, frame)
        break
        

capp.release()
cv.destroyAllWindows()
