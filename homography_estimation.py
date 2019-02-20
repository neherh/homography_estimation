import cv2
import numpy as np
from matplotlib import pyplot as plt

def tellme(s):
    print(s)
    plt.title(s, fontsize=14)
    plt.draw()


imgPts = []
projPts = []

img = cv2.imread('image1.jpg',0)
imgRink = cv2.imread('ice_rink.png',0)

laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

# define first subplot and get points
plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

tellme('Select 4 points on the image')
while True:
    imgPts = []
    while len(imgPts) < 4:
        imgPts = np.asarray(plt.ginput(4, timeout=-1))
        if len(imgPts) < 4:
            tellme('Too few points, starting over')
            time.sleep(1)  # Wait a second

    ph = plt.plot(imgPts[:, 0], imgPts[:, 1], 'ro', lw=2)

    tellme('Happy? Key click for yes, mouse click for no')

    if plt.waitforbuttonpress():
        tellme('Image')
        break

    # Get rid of fill
    for p in ph:
        p.remove()


# define second set of points
plt.subplot(2,2,2),plt.imshow(imgRink,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])

tellme('Select 4 points on the image')
while True:
    projPts = []
    while len(projPts) < 4:
        projPts = np.asarray(plt.ginput(4, timeout=-1))
        if len(projPts) < 4:
            tellme('Too few points, starting over')
            time.sleep(1)  # Wait a second

    ph = plt.plot(projPts[:, 0], projPts[:, 1], 'ro', lw=2)

    tellme('Happy? Key click for yes, mouse click for no')

    if plt.waitforbuttonpress():
        tellme('Field')
        break

    # Get rid of fill
    for p in ph:
        p.remove()


# calculate Homography and apply to image
M, mask = cv2.findHomography(imgPts, projPts, 0, 5.0)
matchesMask = mask.ravel().tolist()

img = img.astype(dtype='float32')
# img = img[np.newaxis,:,:]
M = M.astype(dtype='float32')

print(img.shape)

print(img.dtype)
print(M.dtype)
print(M)
print(mask)
print(M.shape)

a = np.array([[1, 2], [4, 5], [7, 8]], dtype='float32')
h = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype='float32')
a = np.array([a])
print(a.shape)
print(a.dtype)
print(h.shape)
pointsOut = cv2.perspectiveTransform(a, h)

projectedImage = cv2.warpPerspective(img, M, img.shape)

plt.subplot(2,2,3),plt.imshow(projectedImage,cmap = 'gray')
plt.title('Warped'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Projected'), plt.xticks([]), plt.yticks([])

plt.show()


# import argparse
# import cv2


# # initialize the list of reference points and boolean indicating
# # whether cropping is being performed or not
# refPt = []
# cropping = False
 
# def click_and_crop(event, x, y, flags, param):
# 	# grab references to the global variables
# 	global refPt, cropping
 
# 	# if the left mouse button was clicked, record the starting
# 	# (x, y) coordinates and indicate that cropping is being
# 	# performed
# 	if event == cv2.EVENT_LBUTTONDOWN:
# 		refPt = [(x, y)]
# 		cropping = True
 
# 	# check to see if the left mouse button was released
# 	elif event == cv2.EVENT_LBUTTONUP:
# 		# record the ending (x, y) coordinates and indicate that
# 		# the cropping operation is finished
# 		refPt.append((x, y))
# 		cropping = False
 
# 		# draw a rectangle around the region of interest
# 		cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
# 		cv2.imshow("image", image)

# # construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True, help="Path to the image")
# ap.add_argument("-p", "--projection", required=True, help="Path to projection image")
# args = vars(ap.parse_args())

# # instructions:
# print("Select four points on image. Press Spacebar.")
# print("Then select the same corresponding points on the projection image. Press Spacebar")
 
# # load the image, clone it, and setup the mouse callback function
# image = cv2.imread(args["image"])
# clone = image.copy()
# cv2.namedWindow("image")
# cv2.setMouseCallback("image", click_and_crop)
 
# # keep looping until the 'q' key is pressed
# while True:
# 	# display the image and wait for a keypress
# 	cv2.imshow("image", image)
# 	key = cv2.waitKey(1) & 0xFF
 
# 	# if the 'r' key is pressed, reset the cropping region
# 	if key == ord("r"):
# 		image = clone.copy()

# 	# if the 'c' key is pressed, break from the loop
# 	elif key == ord(" "):
# 		break
 
# 	# if the 'c' key is pressed, break from the loop
# 	elif key == ord("c"):
# 		break
 
# # if there are two reference points, then crop the region of interest
# # from teh image and display it
# if len(refPt) == 2:
# 	roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
# 	cv2.imshow("ROI", roi)
# 	cv2.waitKey(0)
 
# # close all open windows
# cv2.destroyAllWindows()