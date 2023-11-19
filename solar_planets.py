import cv2 

img =  cv2.imread("solar-system.jpg")

cv2.putText(img,  
           "Sun",
           (100, 100),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           1.5,  
           (0,0,255)
           )
cv2.putText(img,
            "Mercury",
            (135, 250),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (204,197,194)
            )
cv2.putText(img,
            "Venus",
            (200, 170),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (0,140,255)
            )
cv2.putText(img,
            "Earth",
            (280, 260),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (0,255,0)
            )
cv2.putText(img,
            "Mars",
            (380, 250),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.5,
            (0,0,255)
            )
cv2.putText(img,
            "Jupiter",
            (450, 100),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.75,
            (55,103,105)
            )
cv2.putText(img,
            "Saturn",
            (720, 300),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.75,
            (55,103,105)
            )
cv2.putText(img,
            "Uranus",
            (930,140),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.75,
            (255,0,0)
            )
cv2.putText(img,
            "Neptune",
            (1100,280),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.75,
            (255,0,0)
            )

cv2.imshow("output",img)

cv2.waitKey(0)
