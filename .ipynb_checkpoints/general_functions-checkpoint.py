# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 13:53:57 2018

find and return the file name of the latest version of a file 

Inputs:
    @param file_path: the path of the specific file (string)
    @param file_prefix: prefix of filename (string)

Output:
    @param latest_file: the full path of latest version of the file (string)

Example:
    

@author: Mychal
"""

import glob
import os

def filename_latest_version(file_path, file_prefix):
    list_of_files = glob.glob(os.path.join(file_path, file_prefix + '*')) 
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file
