from __future__ import print_function, division
import os
import torch
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Optional
import pretty_midi
from torch.utils.data import Dataset, DataLoader

class MidiDataset(Dataset):
    """Midi Songs dataset."""

    def __init__(self, root_folder: Optional[str] ='datasets/', sets=[]: List[str], fs=5: int):
        """
        Args:
            root_folder: root for the midi files
            sets (list[string]): names of the set of data to be used
                                 if empty list all under dataset folder is used
            fs (int): fps for note frequency
        """
        self.fs = fs
        self.path = os.path.join('.', root_folder)
        self.sets = sets
        if self.sets == []:
            self.sets = next(os.walk(self.path))[1]
        
        self.filenames = self.getListOfFiles()

            
    def __len__(self):
        return len(self.filenames)

    def getListOfFiles(self) -> List[str]: 
        result = []
        for dirr in self.sets:
            dir_path =os.path.join(self.path, dirr)
            filenames = next(os.walk(dir_path))[2]
            result += [os.path.join(dir_path, f_name) for f_name in filenames]

        return result

    def __getitem__(self, idx: int):
        piano_roll = None
        try:
            midi_pretty_format = pretty_midi.PrettyMIDI(self.filenames[idx])
            piano_midi = midi_pretty_format.instruments[0] #piano only for now TODO: change to multi
            piano_roll = piano_midi.get_piano_roll(fs=self.fs)
        except Exception as e:
            print(e)
            print(f"broken file: {file_name}")
            pass
        else:
            return piano_roll


if __name__ == "__main__":
    midi_dataset = MidiDataset()
