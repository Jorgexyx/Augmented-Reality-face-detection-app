import cv2
import numpy as np

class Pets(object):
    def render(self,image,position):
        #load calibration data
        with np.load('webcam_calibration_output.npz') as X:
            mtx , dist, _, _ = [X[i] for i in ('mtx', 'dist', 'rvecs', 'tvecs')]
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        objp = np.zeros((6*7,3), np.float32)
        objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)
        axis = np.float32([[0,0,0],[0,3,0],[3,3,0],[3,0,0],[0,0,-3],[0,3,-3],[3,3,-3],[3,0,-3]])
        
        #find left image
        x = position[0] * 1.0
        y = position[1] * 1.0
        gray  = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        corners = np.array([x,y])
        
        
    
        #project avator to image plane
       # print(corners)
       # rvecs, tvecs = cv2.solvePnPRansac(objp,corners,mtx,dist)
        rvecs = np.array([x, y, 50.1])
        tvecs = np.array([50.1,50.1,50.1])
        imgpts, _ = cv2.projectPoints(axis,rvecs,tvecs,mtx,dist)
       # imgpts, _ = cv2.projectPoints(axis,ret,corners,mtx,dist)
        
        #draw avatar
        self._draw_pet(image,imgpts)

    def _draw_pet(self,img,imgpts):
        imgpts = np.int32(imgpts).reshape(-1,2)

        #draw floor
        #cv2.drawContours(img,[imgpts[:4]],-1,(200,150,10),-3)
        #draw pillars 
        for i,j in zip(range(4),range(4,8)):
            cv2.line(img,tuple(imgpts[i]),tuple(imgpts[j]),(255),3)

        #draw roof
        cv2.drawContours(img,[imgpts[4:]],-1,(200,150,10),3)
