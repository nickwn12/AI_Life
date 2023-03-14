import pickle
import os
import matplotlib.pyplot as plt
import pandas as pd
import time
col_names = ["Path", "numLinks", "Population", "Fitness",
             "Total Number of Simulations", "Generations", "Days Since Creation"]
my_df = pd.DataFrame(columns=col_names)

dir_list = os.listdir("pickleFolder/")
dir_list.sort(key=lambda x: int(
    x.split("test")[-1].split(".")[0]), reverse=True)
counter = 0
totalSimulations = 0
for dir in dir_list:
    if int(dir.split("test")[-1].split(".")[0]) <= 32:
        continue
        nick = 5
    curPath = "pickleFolder/" + dir
    curphcc = pickle.load(open(curPath, 'rb'))
    bestSolution = curphcc.Get_Best()
    bestCubes = bestSolution.cubes
    curPopulation = len(curphcc.parents)
    curGensTrained = curphcc.generationsTrained
    bestFitness = curphcc.Get_Best_Fitness()
    curTotalSimulations = curGensTrained * curPopulation
    print("Path: " + curPath)
    print("Generations Trained: " + str(curGensTrained))
    print("Population: " + str(curPopulation))
    print("Total Simulations: " + str(curTotalSimulations))
    print("Best Fitness of Model: " + str(bestFitness))

    dictAppended = {}
    ["Path", "numLinks", "Population", "Fitness",
        "Total Number of Simulations", "Generations", "Days Since Creation"]
    dictAppended["Path"] = curPath
    try:
        numLinks = bestCubes.numLinks
    except:
        numLinks = None
    dictAppended["numLinks"] = numLinks
    dictAppended["Population"] = curPopulation
    dictAppended["Fitness"] = bestFitness
    dictAppended["Total Number of Simulations"] = curTotalSimulations
    dictAppended["Generations"] = curGensTrained
    ti_c = (time.time() - os.path.getctime(curPath))/86400
    dictAppended["Days Since Creation"] = ti_c
    # my_df = my_df.append(dictAppended,
    #                ignore_index=True)

    # print("Number of Links: " + str(bestCubes.numLinks))
    # print("Number of Sensors " + str(bestCubes.numSensors))
    print()
    totalSimulations += curTotalSimulations
    # curphcc.Show_Best()

    # curphcc.Show_All()
    # print("File: " + dir)
    # print("Generations: " + str(curphcc.generationsTrained))
    # print("Max Fitness: " + str(curphcc.maxFit))
    # print("\n\n")
    curphcc.listRecordData()
    fileLocation = dir.split(".pkl")[0]
    Y = curphcc.maxFitList

    X = list(range(len(Y)))
    if max(Y) > 0:
        plt.plot(X, Y, '-')
        plt.xlabel("X-axis data")
        plt.ylabel("Y-axis data")
        plt.title('Plot ' + curPath + "\nPopulation: " + str(curPopulation))
        filePath = 'plots/' + fileLocation + '.png'
        plt.savefig(filePath)
        plt.show()
        print("""![Alt text](relative % 20""" +
              filePath + """raw=true "Title")""")
        plt.clf()

    # nick = 5

my_df.to_csv('file1.csv')


print("The total Simulations run was " + str(totalSimulations))

# nick = 5
