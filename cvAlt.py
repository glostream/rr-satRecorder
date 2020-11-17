#!/usr/bin/python3

import cv2
import time
# import requests
import shutil
import os
import glob
import imageio
from PIL import Image

folderName = 'images-2011161036'

# fourcc = cv2.VideoWriter_fourcc(*'MP4V')
# out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640,480))

def createVideo(folderName):
    # command to compile video from images
    # change "-framerate" for more or less frames per second in the video
    # os.system("ffmpeg -loglevel warning -y -framerate 1 -pattern_type glob -i './{}/*.jpg' -c:v libx264 -r 30 -pix_fmt yuv420p satVideo.mp4".format(folderName))
    # command to add logo to video
    # os.system("ffmpeg -loglevel warning -y -i ./satVideo.mp4 -i ./cropped-logo-martinique.jpg -filter_complex '[1]scale=iw*0.45:-1[wm];[0][wm]overlay=W-w-0:0' -r 30 satVideoWithLogo.mp4")
    
    try:
        os.makedirs('./{}-marked'.format(folderName))
    except:
        pass

    logo = Image.open("./cropped-logo-martinique.jpg")
    w, h = logo.size
    newSize = (round(w*0.45), round(h*0.45))
    logo = logo.resize(newSize)

    for f in glob.glob('./{}/*.jpg'.format(folderName)):
        image = Image.open(f)
        W, H = image.size
        pos = (640-newSize[0], 0)
        image.paste(logo, pos)
        image.save('./{}-marked/{}'.format(folderName, f.split("/")[2]))

    
    images = []
    with imageio.get_writer('./satVideo.gif', mode='I', duration=1) as writer:
        for f in glob.glob('./{}-marked/*.jpg'.format(folderName)):
            images.append(f)
        images = sorted(images)

        for f in images:
            image = imageio.imread(f)
            writer.append_data(image)



def main():
    createVideo(folderName)


if __name__ == '__main__':
    main()
