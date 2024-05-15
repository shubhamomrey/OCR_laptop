import pytesseract
import cv2
from PIL import Image
import os
import time
import pyttsx3
language = 'en'


image = cv2.imread('saved_img.jpg')
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\LENOVO\AppData\Tesseract_OCR\tesseract.exe'
string = pytesseract.image_to_string(image)
engine = pyttsx3.init()
rate = engine.getProperty('rate')
print (rate)
engine.setProperty('rate', 125) 
engine.say("hi")
engine.say(string)
engine.runAndWait()

