import pickle
import os

dir_list = os.listdir("pickleFolder/")
dir_list.sort(key=lambda x: int(
    x.split("test")[-1].split(".")[0]), reverse=True)
for dir in dir_list:
    curPath = "pickleFolder/" + dir
    curphcc = pickle.load(open(curPath, 'rb'))
    print("File: " + dir)
    print("Generations: " + str(curphcc.generationsTrained))
    print("Max Fitness: " + str(curphcc.maxFit))
    print("\n\n")

    curphcc.Show_Best()

    nick = 5
