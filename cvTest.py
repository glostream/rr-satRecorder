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
    

    # img_array = []
    # for f in glob.glob('./{}/*.jpg'.format(folderName)):
    #   print(f)
    #   img = cv2.imread(f)
    #   height, width, layers = img.shape
    #   size = (width, height)
    #   img_array.append(img)


    # out = cv2.VideoWriter('project.mp4', cv2.VideoWriter_fourcc('m','p','4','v'), 1, size)

    # for i in range(len(img_array)):
    #   out.write(img_array[i])

    # out.release()


    logo = Image.open("./cropped-logo-martinique.jpg")
    w, h = logo.size
    newSize = (round(w*0.45), round(h*0.45))
    logo = logo.resize(newSize)

    images = []
    for f in glob.glob('./{}/*.jpg'.format(folderName)):
        images.append(f)
    images = sorted(images)


    frames = []
    for i in images:
        frame = Image.open(i)
        frame = frame.convert(mode="RGBA")
        W, H = frame.size
        pos = (640-newSize[0], 0)
        frame.paste(logo, pos)

        frames.append(frame)

    frames[0].save('./satVideo.gif', format='GIF', append_images=frames[1:],
     save_all=True, duration=200, loop=0)



def main():
    createVideo(folderName)


if __name__ == '__main__':
    main()
