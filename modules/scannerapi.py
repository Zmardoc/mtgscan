# scanner

import requests
import os
import json
import time

API_KEY = "K81816986088957"
images = []

def get_image_text(filePath):
	deleteFile = True
	with open(filePath, "rb") as a_file:
		headers = {"apiKey": API_KEY}
		file_dict = {filePath: a_file}
		response = requests.post("https://api.ocr.space/parse/image", files=file_dict, headers=headers).json()
		if response["IsErroredOnProcessing"]:
			print("api error: " + response["ErrorMessage"])
			return

		cardName = response["ParsedResults"][0]["ParsedText"].rstrip()
		if cardName == "":
			deleteFile = False

	if deleteFile:
		os.remove(filePath)

	return cardName

def add_path(path):
    images.append(path)

def scan_and_save_images():
	scan = []
	for filePath in images:
		cardName = get_image_text(filePath)
		if cardName == "":
			print("card name from [" + filePath +"] wasn't recognized")
		else:
			scan.append(cardName)
			print(cardName)

	with open("out/scan_"+time.strftime("%Y%m%d%H%M%S")+".json", 'w+') as outfile:
		json.dump(scan, outfile)
		print(scan)