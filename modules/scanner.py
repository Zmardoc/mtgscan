# scanner

import os
import json
import time
from PIL import Image
import pytesseract
import numpy as np
import modules.image as image

images = []


def get_image_text(filePath):
	convertedImage = image.get_converted_image(filePath)
	return pytesseract.image_to_string(convertedImage, config=r'--oem 3 --psm 6')

def add_path(path):
    images.append(path)

def scan_and_save_images():
	scan = []
	for filePath in images:
		cardName = get_image_text(filePath)
		if cardName == "":
			print("card name from [" + filePath +"] wasn't recognized")
		else:
			os.remove(filePath)
			scan.append(cardName)
			print(cardName)

	with open("out/scan_"+time.strftime("%Y%m%d%H%M%S")+".json", 'w+') as outfile:
		json.dump(scan, outfile)
		print(scan)