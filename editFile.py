import os
from opts import *
def rename(path):
    i=801
    for image in os.listdir(path):
        if 'jpeg' in image:
            os.system("mv {} {}".format(os.path.join(path,image),os.path.join(path,"image_{}.jpeg".format(i))))
            os.system("mv {} {}".format(os.path.join(path,image.replace('jpeg','txt')),os.path.join(path,"image_{}.txt".format(i))))
            i+=1

def trainTxt(path):
    trainFile = open('/home/vinh/Python/hcmaic_tqker/label/train.txt','w+')
    u=1
    for streets in os.listdir(path):
        if 'jpeg' in streets:
                trainFile.write("dataset/images/{image}\n".format(image=streets))
                u+=1
            

if __name__ == "__main__":
    opt = parse_opts()
    path = opt.videos
    trainTxt(path)
