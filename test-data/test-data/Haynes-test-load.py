# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 11:36:11 2023

@author: dahaynes
"""

import glob
## library for cycling through a directory of files
## import geopandas
## a spatial support for pandas
import pandas as pd
## data frame
from pathlib import Path



############## CODE STARTS ###################
## Raw string  
theRootDir = r"E:\git\champion-database-loading"
theDataDirectory = "test-data"

r = Path(theRootDir)

theDataDir = r.joinpath(theDataDirectory)
##WindowsPath('E:/git/champion-database-loading/test-data')

## Now we have the paths of all CSV files
items = theDataDir.glob(r'*.csv')

## items is a generator, which means you have to have to extract the
## things in side it with a loop.
for i in items:
    print(i)
    
df = pd.read_csv(str(i))


