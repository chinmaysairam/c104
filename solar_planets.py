import cv2
img=cv2.imread("solar-system.jpg")
cv2.putText(img,  
           "mercury",
           (100, 250),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(0,0,255)
           )
cv2.putText(img,  
           "venus",
           (190, 250),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(0,0,255)
           )
cv2.putText(img,  
           "earth",
           (300, 250),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(0,0,255)
           )
cv2.putText(img,  
           "mars",
           (380, 250),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(0,0,255)
           )
cv2.putText(img,  
           "jupiter",
           (540, 350),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(0,0,255)
           )
cv2.putText(img,  
           "saturn",
           (740, 270),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(0,0,255)
           )
cv2.putText(img,  
           "uranus",
           (1000, 280),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(0,0,255)
           )
cv2.putText(img,  
           "neptune",
           (1100, 280),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(0,0,255)
           )                                                                             
cv2.imshow("output",img)
cv2.waitKey(0)
