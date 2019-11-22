from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image
from PIL import ImageEnhance
import numpy as np
from cv2 import cv2
# from matplotlib import pyplot as plt
# import matplotlib.image as mpimg
# import matplotlib.pyplot as plt
import dlg
import histogram as h
import cumulative_histogram as ch
import math
import mysql.connector
import os

mydb1 = mysql.connector.connect(
    host="localhost",
    user="idodo",
    passwd="idodo123",
    database="image"
)
mycursor1 = mydb1.cursor(buffered=True)


def setImage(self):
    global fileName,files
    display1 = """select * from imageinfo order by id desc"""
    mycursor1.execute(display1, )
    disp = mycursor1.fetchone()
    disps = [row for row in disp]
    print(disps[6])
    files = str(disps[6])
    # fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
    #     None, "Select Image", "", "Image Files (*.png *.jpg *jpeg *.bmp)")  # Ask for file
    # if fileName:  # If the user gives a file
        # Setup pixmap with the provided image
    pixmap = QtGui.QPixmap(files)
    pixmap = pixmap.scaled(self.imagelab1.width(), self.imagelab1.height(), QtCore.Qt.KeepAspectRatio)  # Scale pixmap
    self.imagelab1.setPixmap(pixmap)  # Set the pixmap onto the label
    self.imagelab1.setAlignment(QtCore.Qt.AlignCenter)


def noise(self):
    image = Image.open(files)
    image.save("a.png")
    img = cv2.imread("a.png")

    median = cv2.medianBlur(img, 5)
    cv2.imwrite("output/output.png", median)

    pixmap = QtGui.QPixmap("output/output.png") # Setup pixmap with the provided image
    pixmap = pixmap.scaled(self.imagelab2.width(), self.imagelab2.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
    self.imagelab2.setPixmap(pixmap) # Set the pixmap onto the label
    self.imagelab2.setAlignment(QtCore.Qt.AlignCenter)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def mac(self):

    image = Image.open(files)
    image.save("c.png")
    img = cv2.imread('c.png', cv2.IMREAD_GRAYSCALE)

    height = img.shape[0]
    width = img.shape[1]
    pixels = width * height

    hist = h.histogram(img)
    cum_hist = ch.cumulative_histogram(hist)

    p = 0.005

    a_low = 0
    for i in np.arange(256):
        if cum_hist[i] >= pixels * p:
            a_low = i
            break

    a_high = 255
    for i in np.arange(255, -1, -1):
        if cum_hist[i] <= pixels * (1 - p):
            a_high = i
            break

    for i in np.arange(height):
        for j in np.arange(width):
            a = img.item(i, j)
            b = 0
            if a <= a_low:
                b = 0
            elif a >= a_high:
                b = 255
            else:
                b = float(a - a_low) / (a_high - a_low) * 255
            img.itemset((i, j), b)

    cv2.imwrite('output/output.png', img)
    pixmap = QtGui.QPixmap("output/output.png") # Setup pixmap with the provided image
    pixmap = pixmap.scaled(self.imagelab2.width(), self.imagelab2.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
    self.imagelab2.setPixmap(pixmap) # Set the pixmap onto the label
    self.imagelab2.setAlignment(QtCore.Qt.AlignCenter)

    #cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def scc(self):

    image = Image.open(files)
    image.save("c.png")
    img = cv2.imread('c.png', cv2.IMREAD_GRAYSCALE)

    height = img.shape[0]
    width = img.shape[1]

    contrast = 2.5

    for i in np.arange(height):
        for j in np.arange(width):
            a = img.item(i, j)
            b = math.ceil(a * contrast)
            if b > 255:
                b = 255
            img.itemset((i, j), b)

    cv2.imwrite('output/output.png', img)
    pixmap = QtGui.QPixmap("output/output.png") # Setup pixmap with the provided image
    pixmap = pixmap.scaled(self.imagelab2.width(), self.imagelab2.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
    self.imagelab2.setPixmap(pixmap) # Set the pixmap onto the label
    self.imagelab2.setAlignment(QtCore.Qt.AlignCenter)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def median_new(self):

    image = Image.open(files)
    image.save("c.png")
    img = cv2.imread('c.png', cv2.IMREAD_GRAYSCALE)
    img_out = img.copy()

    height = img.shape[0]
    width = img.shape[1]

    for i in np.arange(3, height-3):
        for j in np.arange(3, width-3):
            neighbors = []
            for k in np.arange(-3, 4):
                for l in np.arange(-3, 4):
                    a = img.item(i+k, j+l)
                    neighbors.append(a)
            neighbors.sort()
            median = neighbors[24]
            b = median
            img_out.itemset((i,j), b)

    cv2.imwrite('output/output.png', img_out)



    pixmap = QtGui.QPixmap("output/output.png", img_out) # Setup pixmap with the provided image
    pixmap = pixmap.scaled(self.imagelab2.width(), self.imagelab2.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
    self.imagelab2.setPixmap(pixmap) # Set the pixmap onto the label
    self.imagelab2.setAlignment(QtCore.Qt.AlignCenter)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def max(self):
    image = Image.open(files)
    image.save("c.png")
    img = cv2.imread('c.png', cv2.IMREAD_GRAYSCALE)


    img_out = img.copy()

    height = img.shape[0]
    width = img.shape[1]

    for i in np.arange(3, height-3):
        for j in np.arange(3, width-3):
            max = 0
            for k in np.arange(-3, 4):
                for l in np.arange(-3, 4):
                    a = img.item(i+k, j+l)
                    if a > max:
                       max = a
            b = max
            img_out.itemset((i,j), b)



    cv2.imwrite('output/output.png', img_out)
    pixmap = QtGui.QPixmap("output/output.png", img_out) # Setup pixmap with the provided image
    pixmap = pixmap.scaled(self.imagelab2.width(), self.imagelab2.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
    self.imagelab2.setPixmap(pixmap) # Set the pixmap onto the label
    self.imagelab2.setAlignment(QtCore.Qt.AlignCenter)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def min(self):
    image = Image.open(files)
    image.save("c.png")
    img = cv2.imread('c.png', cv2.IMREAD_GRAYSCALE)



    img_out = img.copy()

    height = img.shape[0]
    width = img.shape[1]

    for i in np.arange(3, height-3):
        for j in np.arange(3, width-3):
            min = 255
            for k in np.arange(-3, 4):
                for l in np.arange(-3, 4):
                    a = img.item(i+k, j+l)
                    if a < min:
                       min = a
            b = min
            img_out.itemset((i,j), b)
    cv2.imwrite('output/output.png', img_out)
    pixmap = QtGui.QPixmap("output/output.png", img_out) # Setup pixmap with the provided image
    pixmap = pixmap.scaled(self.imagelab2.width(), self.imagelab2.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
    self.imagelab2.setPixmap(pixmap) # Set the pixmap onto the label
    self.imagelab2.setAlignment(QtCore.Qt.AlignCenter)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


