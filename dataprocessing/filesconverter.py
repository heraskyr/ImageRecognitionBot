import os

from pyrlottie import LottieFile, convSingleLottie, run
import cv2
from os import listdir, remove
from os.path import isfile, join
import cv2

yes_no_list = ['no/', 'yes/']
root = './../files/train/'
animated = 'animated/'
yesanim = "files/yesanim/"
noanim = "files/noanim/"

gif = 'gif/'
dim = (256, 256)


def tgs_to_frames(path, name):
    out = path+animated+name.replace("tgs", "gif")
    file = LottieFile(path+animated+name)
    run(convSingleLottie(file, destFiles={out}))
    vidcap = cv2.VideoCapture(out)
    success, image = vidcap.read()
    count = 0
    while success:
        if(count%5==0):
            filename = path+name.replace(".tgs", "") + "_frame_" + str(count) + '.png'
            image = cv2.resize(image, dim)
            cv2.imwrite(filename, image)  # save frame as webp file
        success, image = vidcap.read()
        count += 1
    vidcap = None
    os.remove(out)
    os.remove(path+animated+name)
    print("ok")

def webmtoframes(path, name):
    vidcap = cv2.VideoCapture(path+name)
    success, image = vidcap.read()
    count = 0
    while success:
        if (count % 3 == 0):
            filename = no +'processed/'+ name.replace(".webm", "") + "_frame_" + str(count) + '.png'
            image = cv2.resize(image, dim)
            cv2.imwrite(filename, image)  # save frame as JPEG file
        success, image = vidcap.read()
        count += 1
    vidcap = None
    os.remove(path+name)
    print("ok")


async def getSingleFrame(path):
    file = LottieFile(path)
    out = path.replace("tgs","gif")
    await convSingleLottie(file, destFiles={out})
    vidcap = cv2.VideoCapture(out)
    success, image = vidcap.read()
    cv2.imwrite(path.replace('tgs', 'png'), image)
    return path.replace('tgs', 'png')

def convert_all_tgs_to_frames():
    from os import listdir, remove
    from os.path import isfile, join
    for  yes_no in yes_no_list:
        path = root+yes_no
        path_animated = path+animated
        files = [f for f in listdir(path_animated) if isfile(join(path_animated, f))]
        for file in files:
            print(path+file)
            tgs_to_frames(path, file)
        print(f"Converted all in {yes_no}")
    print("Finished")

def convertallwebmtoframes():
    from os import listdir, remove
    from os.path import isfile, join
    path='files/noanim/'
    files = [f for f in listdir(path) if isfile(join(path, f))]
    for file in files:
        print(path+file)
        webmtoframes(path, file)
        print("Converted")
    print("Finished")



def resizeall():
    for path in paths:
        files = [f for f in listdir(path) if isfile(join(path, f))]
        for file in files:
            fpath = path+'/'+file
            npath = path+'/processed/'+file
            image = cv2.imread(fpath, cv2.IMREAD_COLOR)
            dim = (256,256)
            nimage = cv2.resize(image, dim)
            remove(fpath)
            cv2.imwrite(npath, nimage)
            #print(file + " finished")
    print("Finished resizing")


# def resize(path, file):
#     fpath = path + '/' + file
#     npath = path + '/processed/' + file
#     # print(fpath)
#     image = cv2.imread(fpath, cv2.IMREAD_COLOR)
#     dim = (256, 256)
#     nimage = cv2.resize(image, dim)
#     print(nimage.shape)
#     remove(fpath)
#     cv2.imwrite(npath, nimage)

convert_all_tgs_to_frames()
#convertallwebmtoframes()
#resizeall()
