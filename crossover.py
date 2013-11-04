import random
crossOverPoints=3
crossOverProbability=30
def crossover(schedule1,schedule2):
#	if(random.random()*100>crossOverProbability):	
#		return schedule1
	cpoints=[]
	low = 0;

#	high = len(globalScheduleMap[0].keys())-1
	high=10
	for i in range(crossOverPoints):
		cpoints+=[random.randint(low,high)-1]
		low = cpoints[i]
		if(low<high):
			low+=1
#	print cpoints
	isSwitchMap=0
	cpointCounter=0
	newSchedule={}
	for i in range(high):
#		print str(i)+","+str(isSwitchMap)+","+str(cpointCounter)+","+str(schedule1.keys()[i])
		if(cpointCounter<len(cpoints)):
			if(isSwitchMap==0):
				key=schedule1.keys()[i]
				newSchedule[key]=schedule1[key]
			else:
				key=schedule2.keys()[i]
				newSchedule[key]=schedule2[key]
			if(i==cpoints[cpointCounter]):
				cpointCounter+=1
				isSwitchMap=1-isSwitchMap
		else:
			if(isSwitchMap==0):
				key=schedule1.keys()[i]
				newSchedule[key]=schedule1[key]
			else:
				key=schedule2.keys()[i]
				newSchedule[key]=schedule2[key]
			
	return newSchedule
