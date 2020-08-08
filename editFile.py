import os
from opts import *
def rename(path):
    i=1
    for image in os.listdir(path):
        os.system("mv {} {}".format(os.path.join(path,image),os.path.join(path,"image_{}.jpeg".format(i))))
        i+=1

def trainTxt(path):
    trainFile = open('/home/vinh/Python/hcmaic_tqker/label/train.txt','w+')
    u=1
    for image in os.listdir(path):
        if 'jpeg' in image:
            trainFile.write("/content/hcmaic_tqker/frames/image_{}.jpeg\n".format(u))
            u+=1

if __name__ == "__main__":
    opt = parse_opts()
    path = opt.videos
    trainTxt(path)
