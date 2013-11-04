#Declaring Constants
crossOverPoints=3
crossOverProbability=30
mutationPoints=5
mutationProbability=30
requiredFitness = 0.8
timeSlotsList = ["S"+str(i) for i in range(1,7)]
dayList = ["D"+str(i) for i in range(1,7)]
numInitialSelectedSchedules=2
initialNumberOfTimeTables=10

#Declaring Global Varibles
studentListMap ={}
courseFacultyListMap = {}
timeTableSchedule = {}
roomNumberList = []
courseList = []
globalScheduleMap ={}
sortedGlobalScheduleMapList=[]

from readData import *
from generateRandomTimeTables import *
from fitness import *
from crossover import *
import operator
## This method populates the roomNumberList, studentListMap, 
## courseFacultyListMap, courseList
readData()

## Once we have populated our data structures with the static data fom the given input files, 
## our next task is to generate a random timeTableSchedules which act as our initial solution.
## These initial timeTableSchedules are populated in the globalScheduleMap 

generateRandomTimeTableSchedules()

## Now we have to sort the globalScheduleMap on value i.e fitness.
## But as a map has no order inherently, it would be a wise decision
## to get a sorted list of tuples of the form [(timeTableSchedule,fitness)],
## where the elements of the list are sorted on the fitness value

sortedGlobalScheduleMapList=sorted(globalScheduleMap.iteritems(),key=operator.itemgetter(1),reverse=True)

while(sortedGlobalScheduleMapList[0][1]<=requiredFitness):
		## Now perform crossover of first numInitialSelectedSchedules pairs of schedules and store them in a list 
		newTimeTablesList=[]
		for i in range(numInitialSelectedSchedules):
			newTimeTablesList+=[crossover(sortedGlobalScheduleMapList[2*i][0],sortedGlobalScheduleMapList[2*i+1][0])]
			
		## Perform mutation of the generated Time Tables
		for i in range(len(newTimeTablesList)):
			newTimeTablesList[i]=mutate(newTimeTablesList[i])

		## Check if the mutated time tables finess is better than the timetable with least fitness in the sortedGlobalScheduleMapList
		## If so replace that time table in the globalScheduleMap with the current map
		## else skip the current map
		for i in range (len(newTimeTablesList)):
			curFitness=fitness(newTimeTablesList[i])
			if curFitness>sortedGlobalScheduleMapList[len(sortedGlobalScheduleMapList)-1][1]):
				globalScheduleMap.pop(sortedGlobalScheduleMapList[len(sortedGlobalScheduleMapList)-1][0])
				globalScheduleMap[newTimeTablesList[i]]=curFitness
				## Update the sortedGlobalScheduleMapList as the globalScheduleMap is updated
				sortedGlobalScheduleMapList=sorted(globalScheduleMap.iteritems(),key=operator.itemgetter(1),reverse=True)

print "Timetable Schedule is finalized with required Fitness"
print sortedGlobalScheduleMapList[0][0]
