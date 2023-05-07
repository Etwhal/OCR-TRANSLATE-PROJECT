from PIL import Image

import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

import numpy as np
import refining_image

import cv2
import deepl_func

translator = deepl_func.__init__()
filename = "imgs\\rei_jap.png"

img2 = cv2.imread(filename)[470: 680, 0:735]

def ocr_core(img):
    text = pytesseract.image_to_string(img, 'jpn')
    return text



img2 = refining_image.get_greyscale(img2)
#img2 = adap_gausse(img2)
#img2 = erosion(img2)
#img2 = gaussian_blur(img2)
#img2 = thresholding(img2)
img2 = refining_image.reduce_noise_2(img2)


cv2.imshow("ratio", img2)
cv2.waitKey(0)

translated = ocr_core(img2)
print("translated text is : " + translated)

#result = translator.translate_text(translated, target_lang="FR")
#print(result.text)