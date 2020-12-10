import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from midi2img.midi2img import Midi2Img
from midi2img.img2midi import Img2Midi
from music21 import midi
from tqdm import tqdm 

def main():
    data_dir = 'data/output_imgs/out_style_transferred/classical'
    num_files = len(os.listdir(data_dir))
    file_list = os.listdir(data_dir)
    for i in tqdm(range(len(file_list))):
        filename = file_list[i]
        if filename.endswith('.png'):
            try:
                i2m = Img2Midi(os.path.join(data_dir, filename))
                i2m.image2midi(outdir = 'data/output_midi/out_style_transferred/classical')
            except:
                print("Img file could not be read: ", filename)
            print("Processed {} out of {}".format(i, num_files))

    data_dir = 'data/output_imgs/out_style_transferred/jazz'
    num_files = len(os.listdir(data_dir))
    file_list = os.listdir(data_dir)
    for i in tqdm(range(len(file_list))):
        filename = file_list[i]
        if filename.endswith('.png'):
            try:
                i2m = Img2Midi(os.path.join(data_dir, filename))
                i2m.image2midi(outdir = 'data/output_midi/out_style_transferred/jazz')
            except:
                print("Img file could not be read: ", filename)
            print("Processed {} out of {}".format(i, num_files))
    
    data_dir = 'data/output_imgs/out_superposed/classical'
    num_files = len(os.listdir(data_dir))
    file_list = os.listdir(data_dir)
    for i in tqdm(range(len(file_list))):
        filename = file_list[i]
        if filename.endswith('.png'):
            try:
                i2m = Img2Midi(os.path.join(data_dir, filename))
                i2m.image2midi(outdir = 'data/output_midi/out_superposed/classical')
            except:
                print("Img file could not be read: ", filename)
            print("Processed {} out of {}".format(i, num_files))

    data_dir = 'data/output_imgs/out_superposed/jazz'
    num_files = len(os.listdir(data_dir))
    file_list = os.listdir(data_dir)
    for i in tqdm(range(len(file_list))):
        filename = file_list[i]
        if filename.endswith('.png'):
            try:
                i2m = Img2Midi(os.path.join(data_dir, filename))
                i2m.image2midi(outdir = 'data/output_midi/out_superposed/jazz')
            except:
                print("Img file could not be read: ", filename)
            print("Processed {} out of {}".format(i, num_files))

if __name__=="__main__": 
    main()