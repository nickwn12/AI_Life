
# Evolving Walker

This project was created so that I could make a robot that would be able to walk/crawl effectivly as well as being able to evolve physically as it kept on improving. 

Building a robot

# Cubes Class

To build the Robot I created a new class called Cubes. This was both inspired by Carl Simins designs where I loved the way that his robots looked and I also felt like that if I made the designs cubes it would make the math and creation of the robots easier allowing me to spend more time on the interesting parts of the project. 

The Cubes class would have a self.weights to control and create the brain. It would have a tree of parents which would keep the ordering of which cubes had which parents. It would contain a list of everysingle cube its height, length, width, as well as the data concering if each cube was a sensor or a not. This was all put in a class called Cube. Cubes was a a collection of Cube. The Cubes class could create a robot create the body and the brain. 

When I made this change I had to 
## Cube Class
Each Cube had a few specfic parts of it. This included its length, width, and height. The cube also had its centerX, centerY, and centerZ all together in order to make sure that you could calculate if cubes were intersecting. 

If you have access to the center location of the cube as well as its dimentions you can do a pretty easy check to see if the cube would would interact with one other cube. You can also use this to see if the Cube would be bellow the ground. When you add cubes to the class you make sure that the new cube both would not intercept with any other cubes as well as 

These are some diagrams of how the rules for cubes work
![Screenshot](/ReadMeImages/oneBox.png)

If you add an initial cube that gets added onto the orignal cube if it passes the requirements
diagramed below
![Screenshot](/ReadMeImages/twoBoxs.png)


![Screenshot](/ReadMeImages/IlligalUnder.png)
If you add in a cubes so that they are under 0 the cube will not be palced and you
will add cubes until one is sucessfuly added so that its lowest z point is not below 0

![Screenshot](/ReadMeImages/overlap.png)

If you add in two cubes so that they would overlap it cancles it out.
And puts in a new cube until a cube is succesfuly added

## Mutation of the Cubes

The cubes are mutated in two main ways. Either I am changing the shapes of one of the cubes or I am changing the brain. This allows for you to get some very interesting designs that show off how things move as well as the joints that exist. One of the problems with this however is that it is not deleting or adding cubes because that would make me change the brain in ways that would alter how the rest of the robot was working. This is one of the largest flaws that exist in my robot right now and if I were able to have more time to work on this assignment and or something I will implement for the final project is adding in a way for me to create and destroy cubes along with the rest of the robot. 
## Selection Algorithm
One of the largest problems that I had with this algorithm was that you would have pleanty of designs that just apeared as thoguh they were not able to work and was using computing power in a useless way. My way around this contraint was to have the robots that was preforming worse be replaced with a random other robot. I experemented with trying to replace the worst one with the best one but the problem with this method was that you would get tons of clones of the best robot which would kill your genetic diversity. This way you should still allow for some level of diveristy but the robtots that were not showing any promise were cut. 
## Things to Add on in the future
I would want to add on a competition between the robots or find a way to optomise the selection formula so that you can both have lots of diversity but still focus on the stronger designs. 


I would want to make it so that the body could evolve to grow and shrink so that the brain can grow and shrink without destorying the body. To do this I would need to redesign some portions of the cube system as well as adding on.

I would also want to make it so that the sensors could change from one link to anouther link. This would involve moving the sensors from being decided in the constants to being an internal part of the designs which would be possible but once again difficult. A lot of these changes would involve reformating most of my code for interesting benifits but would be a large investment of time. 

I also would want to go to office hours to try and figure out how to avoid platus where the design seems like it can not get any better with more mutations but I know that there has to be a better way for the design to work. Or finding ways to encurage the robot to walk or have its center of mass as high as possible at the end of the 
## How to Run 
There is a function called the searchCubes function
All you need to do is run this function in order to show a random body before training. Evolve the model then show the best model of the ones that you have trained already. 
The settings for the number of links, scaling settings, motor strength, number of gerations, as well as populaiton can all be controlled from the contants

## Graphs of Generations

Individual Graphs
![Screenshot](/ReadMeImages/Figure_1.png)
![Screenshot](/ReadMeImages/Figure_2.png)
![Screenshot](/ReadMeImages/Figure_3.png)
![Screenshot](/ReadMeImages/Figure_4.png)
![Screenshot](/ReadMeImages/Figure_5.png)
![Screenshot](/ReadMeImages/Combined.png)

The results is that I have found that there will be times when the robots will preform much better or worse. I think that this is some level of unpredictablity in the physics simulator but a lot of these machines will be capible of doing amazing things in some runs and with the same body and brain it will do signifigantly worse. I do not know if there is a way to select for this better. But the two things I would add to deal with that would be the sin function of time so it knew where it was in a cycle and did not need to rely on rythic sensor pullings in order to get data from. I would also train it for much much longer. 




## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)

https://www.tinkercad.com/things/ was extremely useful for making the 3d diagrams 

I also wanted to Acknowledge that I took advantage of the advice that you gave in lecture to help me. 

## Authors

- [@octokatherine](https://www.github.com/octokatherine)


Path: pickleFolder/test69.pkl
Generations Trained: 200
Population: 10
Total Simulations: 2000
Best Fitness of Model: 19.301054933851532

![Alt text](relative % 20plots/test69.pngraw=true "Title")
Path: pickleFolder/test68.pkl
Generations Trained: 200
Population: 10
Total Simulations: 2000
Best Fitness of Model: 7.371755589279394

![Alt text](relative % 20plots/test68.pngraw=true "Title")
Path: pickleFolder/test67.pkl
Generations Trained: 200
Population: 10
Total Simulations: 2000
Best Fitness of Model: 11.374880990639998

![Alt text](relative % 20plots/test67.pngraw=true "Title")
Path: pickleFolder/test66.pkl
Generations Trained: 200
Population: 10
Total Simulations: 2000
Best Fitness of Model: 6.969525415513104

![Screenshot](plots/test66.pngraw=true "Title")
Path: pickleFolder/test65.pkl
Generations Trained: 50
Population: 50
Total Simulations: 2500
Best Fitness of Model: 9.105079390305512

![Alt text](relative % 20plots/test65.pngraw=true "Title")
Path: pickleFolder/test64.pkl
Generations Trained: 50
Population: 50
Total Simulations: 2500
Best Fitness of Model: 11.580110052813495

![Alt text](relative % 20plots/test64.pngraw=true "Title")
Path: pickleFolder/test63.pkl
Generations Trained: 50
Population: 10
Total Simulations: 500
Best Fitness of Model: 3.9260061237295454

![Alt text](relative % 20plots/test63.pngraw=true "Title")
Path: pickleFolder/test62.pkl
Generations Trained: 500
Population: 10
Total Simulations: 5000
Best Fitness of Model: 11.466548383868778

![Alt text](relative % 20plots/test62.pngraw=true "Title")
Path: pickleFolder/test61.pkl
Generations Trained: 500
Population: 10
Total Simulations: 5000
Best Fitness of Model: 12.949485588748605

![Alt text](relative % 20plots/test61.pngraw=true "Title")
Path: pickleFolder/test60.pkl
Generations Trained: 500
Population: 10
Total Simulations: 5000
Best Fitness of Model: 10.504130684149974

Path: pickleFolder/test59.pkl
Generations Trained: 200
Population: 25
Total Simulations: 5000
Best Fitness of Model: 25.99498191365418

Path: pickleFolder/test58.pkl
Generations Trained: 200
Population: 25
Total Simulations: 5000
Best Fitness of Model: 17.015708174629516

Path: pickleFolder/test57.pkl
Generations Trained: 100
Population: 10
Total Simulations: 1000
Best Fitness of Model: 5.803501041868914

Path: pickleFolder/test56.pkl
Generations Trained: 100
Population: 10
Total Simulations: 1000
Best Fitness of Model: 5.4811631830241385

Path: pickleFolder/test55.pkl
Generations Trained: 100
Population: 10
Total Simulations: 1000
Best Fitness of Model: 13.59828398706952

Path: pickleFolder/test54.pkl
Generations Trained: 100
Population: 10
Total Simulations: 1000
Best Fitness of Model: 7.282209728287096

Path: pickleFolder/test53.pkl
Generations Trained: 100
Population: 10
Total Simulations: 1000
Best Fitness of Model: 5.601628893405993

Path: pickleFolder/test52.pkl
Generations Trained: 100
Population: 10
Total Simulations: 1000
Best Fitness of Model: 6.094847085421369

Path: pickleFolder/test51.pkl
Generations Trained: 100
Population: 10
Total Simulations: 1000
Best Fitness of Model: 7.134761360379178

Path: pickleFolder/test50.pkl
Generations Trained: 100
Population: 10
Total Simulations: 1000
Best Fitness of Model: 8.549638168845032

Path: pickleFolder/test49.pkl
Generations Trained: 100
Population: 10
Total Simulations: 1000
Best Fitness of Model: 8.385577491287986

Path: pickleFolder/test48.pkl
Generations Trained: 500
Population: 10
Total Simulations: 5000
Best Fitness of Model: 17.500675259816738

Path: pickleFolder/test47.pkl
Generations Trained: 500
Population: 10
Total Simulations: 5000
Best Fitness of Model: 7.957729572482561

Path: pickleFolder/test46.pkl
Generations Trained: 100
Population: 10
Total Simulations: 1000
Best Fitness of Model: 18.85316928507671

Path: pickleFolder/test45.pkl
Generations Trained: 500
Population: 10
Total Simulations: 5000
Best Fitness of Model: 4.483399110661695

Path: pickleFolder/test44.pkl
Generations Trained: 500
Population: 10
Total Simulations: 5000
Best Fitness of Model: 8.851402238025642

Path: pickleFolder/test43.pkl
Generations Trained: 500
Population: 10
Total Simulations: 5000
Best Fitness of Model: 9.052847871349405

Path: pickleFolder/test42.pkl
Generations Trained: 500
Population: 10
Total Simulations: 5000
Best Fitness of Model: 8.737500734802088

Path: pickleFolder/test41.pkl
Generations Trained: 100
Population: 10
Total Simulations: 1000
Best Fitness of Model: 7.563675481227737

Path: pickleFolder/test40.pkl
Generations Trained: 100
Population: 10
Total Simulations: 1000
Best Fitness of Model: 5.100512449003548

Path: pickleFolder/test39.pkl
Generations Trained: 100
Population: 5
Total Simulations: 500
Best Fitness of Model: 4.063378192392414

Path: pickleFolder/test38.pkl
Generations Trained: 300
Population: 25
Total Simulations: 7500
Best Fitness of Model: 6.562502111004393

Path: pickleFolder/test37.pkl
Generations Trained: 300
Population: 25
Total Simulations: 7500
Best Fitness of Model: 7.324944974026716

Path: pickleFolder/test36.pkl
Generations Trained: 300
Population: 25
Total Simulations: 7500
Best Fitness of Model: 12.21181680529474

Path: pickleFolder/test35.pkl
Generations Trained: 200
Population: 10
Total Simulations: 2000
Best Fitness of Model: 7.614822129399039

Path: pickleFolder/test34.pkl
Generations Trained: 200
Population: 10
Total Simulations: 2000
Best Fitness of Model: 7.75795958553575

Path: pickleFolder/test33.pkl
Generations Trained: 200
Population: 10
Total Simulations: 2000
Best Fitness of Model: 12.820376490749497

The total Simulations run was 109500