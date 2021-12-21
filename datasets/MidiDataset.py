from __future__ import print_function, division
import os
import torch
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Optional
from torch.utils.data import Dataset, DataLoader

class MidiDataset(Dataset):
    """Midi Songs dataset."""

    def __init__(self, root_folder: Optional[str] ='datasets/', sets=[]: List[str]):
        """
        Args:
            sets (list[string]): names of the set of data to be used
                                 if empty list all under dataset folder is used
        """
        self.root_dir = root_folder
        self.sets = sets
        if self.sets == []:
            pass
            
            

    def getListOfFiles(dirName): 
        pass
