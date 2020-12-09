import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from midi2img.midi2img import Midi2Img
from midi2img.img2midi import Img2Midi
from music21 import midi
from tqdm import tqdm 

def main():
    data_dir = 'data/images/classical'
    num_files = len(os.listdir(data_dir))
    file_list = os.listdir(data_dir)
    for i in tqdm(range(len(file_list))):
        filename = file_list[i]
        if filename.endswith('.png'):
            try:
                i2m = Img2Midi(os.path.join(data_dir, filename))
                i2m.image2midi(outdir = 'data/converted_midi/classical')
            except:
                print("Midi file could not be read: ", filename)
            print("Processed {} out of {}".format(i, num_files))

    data_dir = 'data/images/jazz'
    num_files = len(os.listdir(data_dir))
    file_list = os.listdir(data_dir)
    for i in tqdm(range(len(file_list))):
        filename = file_list[i]
        if filename.endswith('.png'):
            try:
                i2m = Img2Midi(os.path.join(data_dir, filename))
                i2m.image2midi(outdir = 'data/converted_midi/jazz')
            except:
                print("Midi file could not be read: ", filename)
            print("Processed {} out of {}".format(i, num_files))

if __name__=="__main__": 
    main()