import mss.tools
import mss
from pixel import pix
import os

def get_capture():
    
    #conversion of pixel coordinates for mss
    x1,y1,x2,y2 = pix()
    width = x2-x1
    height = y2-y1

    region = {
        "left":x1,
        "top":y1,
        "width":width,
        "height":height
    }
    
    def capture():

        #current directory
        dir = os.path.dirname(__file__)

        #process of saving a screenshot 
        with mss.mss() as sct:
            monitor = region
            img = sct.grab(monitor)
            #create a dir for image
            if os.path.exists(dir+"/images") == False:
                os.mkdir("images")   
            output = "images/screen.png"
            mss.tools.to_png(img.rgb,img.size,output=output)
            print("Image captured")
    
    return capture
