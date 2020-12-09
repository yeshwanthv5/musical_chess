import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from midi2img.midi2img import Midi2Img
from midi2img.img2midi import Img2Midi
from music21 import midi
from tqdm import tqdm 

def main():
    data_dir = 'data/TPD/jazz'
    jazz = []
    num_files = len(os.listdir(data_dir))
    file_list = os.listdir(data_dir)
    for i in tqdm(range(len(file_list))):
        filename = file_list[i]
        if filename.endswith('.mid'):
            try:
                mid = Midi2Img(os.path.join(data_dir, filename))
                jazz.append(mid)
            except:
                print("Midi file could not be read: ", filename)
            print("Processed {} out of {}".format(i, num_files))

    clips = jazz
    clips = [x for x in clips if x.length > 180]
    img_list = []
    for clip in clips:
        im_list_clip = clip.midi2image("data/images/jazz")
        img_list.append(im_list_clip[0])

if __name__=="__main__": 
    main()