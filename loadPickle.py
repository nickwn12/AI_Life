import pickle
import os
import matplotlib.pyplot as plt

dir_list = os.listdir("pickleFolder/")
dir_list.sort(key=lambda x: int(
    x.split("test")[-1].split(".")[0]), reverse=True)
counter = 0
for dir in dir_list:
    if counter >= 5:
        continue
    curPath = "pickleFolder/" + dir
    curphcc = pickle.load(open(curPath, 'rb'))
    curphcc.Show_All()
    # print("File: " + dir)
    # print("Generations: " + str(curphcc.generationsTrained))
    # print("Max Fitness: " + str(curphcc.maxFit))
    # print("\n\n")
    # curphcc.listRecordData()
    # Y = curphcc.maxFitList
    # X = list(range(len(Y)))
    # plt.plot(X, Y, '-')

    # plt.xlabel("X-axis data")
    # plt.ylabel("Y-axis data")
    # plt.title('multiple plots' + str(counter))
    counter += 1

    nick = 5
# plt.show()
nick = 4
# 

# nick = 5
