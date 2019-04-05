"""
annotate_homography.py

script loads a directory of images, annotates

by Helmut Neher

TODO:
- loop through all images in directory
"""

import json
import codecs
import os

from tkinter import filedialog
from tkinter import *
# # import tkFileDialog
import cv2
import numpy as np
from matplotlib import pyplot as plt

def tellme(s):
    plt.title(s, fontsize=14)
    plt.draw()


# get directory using tkinter gui, then destroy
#https://stackoverflow.com/questions/19944712/browse-for-file-path-in-python
#https://www.youtube.com/watch?v=WTTzN8F5IMI
root = Tk()
currdir = "/home/Documents"
dirName = filedialog.askdirectory(parent=root, initialdir=currdir,
                                        title='Select the directory of your choice by entering into the directory.')
try:
    root.destroy()
except:
    pass


# pertinent variables
imgPts = []
projPts = []
data = {}
toJsonData = {}
imgs =[]


# imgName = 'image1.jpg'
outFile = 'homographyData.json'
imgRink = cv2.imread('ice_rink.png',0)

# get list of images from directory
valid_images = [".jpg",".gif",".png"]
for f in os.listdir(dirName):
    ext = os.path.splitext(f)[1]
    if ext.lower() in valid_images:
        imgs.append([dirName,f])

for imgName in imgs:

    fullImageName = os.path.join(imgName[0],imgName[1])

    # img = cv2.imread(imgName,0)
    img = cv2.imread(fullImageName,0)

    # define first subplot and get points
    plt.clf()
    plt.subplot(2,1,1),plt.imshow(img,cmap = 'gray')
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
    plt.subplot(2,1,2),plt.imshow(imgRink,cmap = 'gray')
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


    # calculate Homography and store values
    # see for serialization: https://stackoverflow.com/questions/26646362/numpy-array-is-not-json-serializable
    homography = cv2.getPerspectiveTransform(imgPts.astype(dtype="float32"),
                                             projPts.astype(dtype="float32")) #- https://stackoverflow.com/questions/11237948/findhomography-getperspectivetransform-getaffinetransform
    data['imgPts']= imgPts.tolist()
    data['projPts'] = projPts.tolist()
    data['homography'] = homography.tolist()

    # add to json dictionary
    toJsonData[imgName[1]] = data


# convert to json and save file
json.dump(toJsonData, codecs.open(outFile,'w', encoding='utf-8'), separators=(',',':'), sort_keys=True, indent = 4)
