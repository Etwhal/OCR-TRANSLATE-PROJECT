import cv2
import numpy as np

def get_greyscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def remove_noise(img):
    return cv2.medianBlur(img, 3)

def gaussian_blur(img):
    return cv2.GaussianBlur(img, (5, 5), 0)

def thresholding(img):
    return cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

def adap_gausse(img):
    return cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

def erosion(img):
    return cv2.erode(img,np.ones((3,3),np.uint8),iterations = 1)

def reduce_noise_2(img):
    return cv2.bilateralFilter(img,9,75,75)