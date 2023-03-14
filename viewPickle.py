import pickle
import os
import matplotlib.pyplot as plt
import pandas as pd
import time

dir_list = os.listdir("pickleFolder/")
dir_list.sort(key=lambda x: int(
    x.split("test")[-1].split(".")[0]), reverse=True)

for dir in dir_list:
    if int(dir.split("test")[-1].split(".")[0]) <= 32:
        continue
    curPath = "pickleFolder/" + dir
    curphcc = pickle.load(open(curPath, 'rb'))
    curphcc.Show_Best()
    waitForInput = input("Ready to Continue?")
