import cv2
import os
from opts import *
import numpy as np
import json

def load_zone_anno(json_filename):
  """
  Load the json with ROI and MOI annotation.

  """
  with open(json_filename) as jsonfile:
    dd = json.load(jsonfile)
    polygon = [[int(x), int(y)] for x, y in dd['shapes'][0]['points']]
    paths = []
    for it in dd['shapes'][1:]:
    #   kk = str(int(it['label'][-2:]))
      paths.append([(int(x), int(y)) for x, y in it['points']]) 
  return polygon, paths


def draw(videos):
    # Create a VideoCapture object and read from input file
    # If the input is the camera, pass 0 instead of the video file name
    cap = cv2.VideoCapture(videos + 'sample_02.mp4')
    fps = cap.get(cv2.CAP_PROP_FPS)
    #Load the json with ROI and MOI annotation.
    polygon, paths = load_zone_anno(videos + 'sample_02.json')
    print(polygon, paths)

    pts = np.array([polygon], np.int32)
    pts = pts.reshape((-1,1,2))
    print(pts)
    # Check if camera opened successfully
    if (cap.isOpened()== False): 
        print("Error opening video stream or file")

    # Read until video is completed
    while(cap.isOpened()):
    # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
            # Display the resulting frame

            #draw polygon
            frame = cv2.polylines(frame,[pts],True,(0,0,255),thickness=3)
            for line in paths:
                frame = cv2.line(frame,line[0],line[1],(0,255,255),thickness=3)
            cv2.imshow('Frame',frame)

            # Press Q on keyboard to  exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        # Break the loop
        else: 
            break

    # When everything done, release the video capture object
    cap.release()

    # Closes all the frames
    cv2.destroyAllWindows()



if __name__ == "__main__":
    opt = parse_opts()
    path = opt.videos
    draw(path)

