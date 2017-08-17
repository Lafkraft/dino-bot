import numpy as np
import cv2
from mss.linux import MSS as mss
from PIL import Image
import time
import pyautogui as pg

# Window Size
#mon = {'top': 20, 'left': 60, 'width': 800, 'height': 400}
mon = {'top': 255, 'left': 240, 'width': 70, 'height': 35}

def process_image(original_image):
    # convert to gray
    processed_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    # edge detection
    processed_image = cv2.Canny(processed_image, threshold1=200, threshold2=300)
    return processed_image

def screen_record():
    sct = mss()
    last_time = time.time()

    while(True):
        img = sct.grab(mon)
        print('loop took {} seconds'.format(time.time() - last_time))
        last_time = time.time()

        img = np.array(img)
        processed_image = process_image(img)

        #                     Height , Width
        # roi = processed_image[235:270,180:250]
        #
        # mean = np.mean(roi)

        mean = np.mean(processed_image)
        print('mean = ', mean)

        if not mean == float(0):
            pg.press('space')

        # gizmo_image = processed_image
        # cv2.rectangle(gizmo_image,(200,180),(250,250),(255,255,255),20)
        # cv2.imshow('Edges', gizmo_image)

        #cv2.imshow('ROI', processed_image)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

screen_record()
