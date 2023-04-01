import numpy as np
import cv2

# Read image
path = r"C:\Users\Lenovo\Pictures\Screenshots\Screenshot (4).png"
img = cv2.imread(path)

# Gaussian blur
blurred = cv2.GaussianBlur(img, (5, 5), 0)
imS = cv2.resize(blurred, (960, 540))
cv2.imshow("output", imS)
cv2.waitKey(0)

# #Convert to graysscale
# gray = cv2.cvtColor(blurred,cv2.COLOR_BGR2GRAY)
# imS = cv2.resize(gray, (960, 540))                # Resize image
# cv2.imshow("output", imS)
# cv2.waitKey(0)


# thresholding brown color
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, (16, 69, 182), (26, 91, 230))
# kernel=np.ones((3,3),np.uint8)
# erosion=cv2.erode(mask,kernel,iterations=1)
imS = cv2.resize(mask, (960, 540))
cv2.imshow("mask", imS)
cv2.waitKey(0)


# #Autocalculate the thresholding level
# threshold = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)


# #Threshold
# retval, bin = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
# imS = cv2.resize(bin, (960, 540))                # Resize image
# cv2.imshow("output", imS)
# cv2.waitKey(0)

# Find contours
contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    if cv2.contourArea(cnt) < 500:
        continue
    if cv2.contourArea(cnt) > 55000:
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(img, [box], 0, (0, 0, 255), 2)
        print(cv2.contourArea(cnt))
        (x, y), (width, height), angleofrotation = cv2.minAreaRect(cnt)
        # print(angleofrotation)
        print(width)
        print(height)
        if width > height:
            print(-angleofrotation + 180)
        else:
            print(-angleofrotation + 90)

    else:
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(img, [box], 0, (0, 191, 255), 2)

    # (x,y,w,h)=cv2.boundingRect(cnt)
    # area=cv2.contourArea(cnt)
    # print (area)

    # if area>55000:
    #     cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    # else:
    #     cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)


imS = cv2.resize(img, (960, 540))
cv2.imshow("output", imS)
cv2.waitKey(0)

# #Sort out the biggest contour (biggest area)
# max_area = 0
# max_index = -1
# index = -1
# for i in contours:
#     area = cv2.contourArea(i)
#     index=index+1
#     if area > max_area :
#         max_area = area
#         max_index = index

# #Draw the raw contours
# contourpic=cv2.drawContours(imS, contours, max_index, (0, 255, 0), 3 )
# cv2.imshow('contours', contourpic)
# cv2.waitKey(0)
# cv2.imwrite("box-1-biggest-contour.png", img)

# #Draw a rotated rectangle of the minimum area enclosing our box (red)
# cnt=contours[max_index]
# rect = cv2.minAreaRect(cnt)
# box = cv2.boxPoints(rect)
# box = np.int0(box)
# img = cv2.drawContours(img,[box],0,(0,0,255),2)

# #Show original picture with contour
# cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
