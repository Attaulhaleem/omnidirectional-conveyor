import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        raise Exception("Video feed not available!")
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # for proper rendering
    frame = cv2.resize(frame, (640, 480))
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

# # #Read image
# # path=r'C:\Users\Lenovo\Documents\FYP\box-1-biggest-contour.png'
# path = r"C:\Users\Lenovo\Pictures\Saved Pictures\pic2.jpg"
# img = cv2.imread(path)

# # Gaussian blur
# blurred = cv2.GaussianBlur(img, (5, 5), 0)
# imS = cv2.resize(blurred, (960, 540))
# cv2.imshow("output", imS)
# cv2.waitKey(0)

# # thresholding brown color
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# # mask = cv2.inRange(hsv, (16,61,179), (22,100,236))
# mask = cv2.inRange(hsv, (0, 62, 0), (179, 255, 255))
# # kernel=np.ones((3,3),np.uint8)
# # erosion=cv2.erode(mask,kernel,iterations=1)
# imS = cv2.resize(mask, (960, 540))
# cv2.imshow("mask", imS)
# cv2.waitKey(0)

# # Find contours
# contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# maxarea = 100
# for cnt in contours:
#     if cv2.contourArea(cnt) < 500:
#         continue
#     if cv2.contourArea(cnt) > 38000:
#         rect = cv2.minAreaRect(cnt)
#         box = cv2.boxPoints(rect)
#         box = np.int0(box)
#         cv2.drawContours(img, [box], 0, (0, 0, 255), 2)
#         print(cv2.contourArea(cnt))
#         (x, y), (width, height), angleofrotation = cv2.minAreaRect(cnt)
#         # print(angleofrotation)
#         print(width)
#         print(height)
#         if width > height:
#             print(-angleofrotation + 180)
#         else:
#             print(-angleofrotation + 90)

#     else:
#         rect = cv2.minAreaRect(cnt)
#         box = cv2.boxPoints(rect)
#         box = np.int0(box)
#         cv2.drawContours(img, [box], 0, (0, 191, 255), 2)
#         # print(cv2.contourArea(cnt))


# imS = cv2.resize(img, (960, 540))
# cv2.imshow("output", imS)
# cv2.waitKey(0)
