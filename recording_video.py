
import cv2 as cv

from datetime import datetime



# current date and time
now = datetime.now()
s1 = now.strftime("%m%d%Y_%H%M%S")


capp = cv.VideoCapture(0, cv.CAP_DSHOW)

filename = f"{s1}" + ".mp4"
codec = cv.VideoWriter_fourcc("M", "P", "4", "V")
fps = 60
res = (640, 480)
savefile = cv.VideoWriter(filename, codec, fps, res)


while True:
    ret, frame = capp.read()
    frame = cv.flip(frame, 1)
        
    savefile.write(frame)

            

    cv.imshow("HaydarCam// click 'q' for close the application", frame)


    if cv.waitKey(30) & 0xFF == ord("q") or 0xFF == ord("Q"):

        break
        
        
savefile.release()
capp.release()
cv.destroyAllWindows()
