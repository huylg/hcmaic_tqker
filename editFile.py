import os
from opts import *
def rename(path):
    i=301
    for image in os.listdir(path):
        if 'jpeg' in image:
            os.system("mv {} {}".format(os.path.join(path,image),os.path.join(path,"image_{}.jpeg".format(i))))
            i+=1

def trainTxt(path):
    trainFile = open('/home/vinh/Python/hcmaic_tqker/label/train.txt','w+')
    u=1
    for streets in os.listdir(path):
        for image in os.listdir(os.path.join(path,streets)):
            if 'jpeg' in image:
                trainFile.write("images/{streets}/{image}\n".format(streets=streets,image=image))
                u+=1

if __name__ == "__main__":
    opt = parse_opts()
    path = opt.videos
    trainTxt(path)
