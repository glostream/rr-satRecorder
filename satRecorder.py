#!/usr/bin/python

import time
import requests
import shutil
import os
import glob
from PIL import Image

imgUrl = "http://www.meteo.fr/temps/domtom/antilles/pack-public/TAG/Tagant.jpg"
# where the image folder is saved
imageFolderPath = "./"
gifFolderPath = "/home/bkwq4309/public_html/anim_archive/"
# change this number to take more or less pictures
numberOfPictures = 96
# frames per second of the GIF
fps = 1


def downloadImage(path, fileName):
	r = requests.get(imgUrl, stream=True)
	if r.status_code == 200:
	    with open("{}/{}.jpg".format(path, fileName), 'wb') as f:
	        r.raw.decode_content = True
	        shutil.copyfileobj(r.raw, f)
	else: print("Something went wrong trying to download the image!")


def cleanImages(path, size):
    images = [f for f in glob.glob('{}/*.jpg'.format(path))]
    if len(images) > size:
	    images = sorted(images)
	    os.remove(images[0])


def createVideo(imageFodlerPath, gifFolderPath):
    logo = Image.open("./cropped-logo-martinique.jpg")
    w, h = logo.size
    newSize = (int(round(w*0.45)), int(round(h*0.45)))
    logo = logo.resize(newSize)

    images = [f for f in glob.glob('{}/*.jpg'.format(imageFodlerPath))]
    images = sorted(images)

    frames = []
    for i in images:
        frame = Image.open(i)
        frame = frame.convert(mode="RGBA")
        W, H = frame.size
        pos = (640-newSize[0], 0)
        frame.paste(logo, pos)
        frames.append(frame)

    frames[0].save('{}satVideo.gif'.format(gifFolderPath), format='GIF', append_images=frames[1:],
     save_all=True, duration=(1/fps)*1000, loop=0)


def main():
	print("Running!")
	timeNow = time.strftime("%y%m%d%H%M", time.localtime())
	folderName = "satRecorder-{}".format(timeNow)
	fullImagePath = imageFolderPath + folderName
	os.makedirs(path)
	while True:
		fileName = time.strftime("%y%m%d%H%M", time.localtime())
		downloadImage(fullImagePath, fileName)
		cleanImages(fullImagePath, numberOfPictures)
		createVideo(fullImagePath, gifFolderPath)
		print("running on {}".format(time.strftime("%d-%m at %H:%M", time.localtime())))
		# pause for 1800 seconds = 30 min before repeating
		time.sleep(1800)


if __name__ == '__main__':
	main()
