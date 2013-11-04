import random
initialNumberOfTimeTables=10

for i in initialNumberOfTimeTables:
	tempScheduleMap={}
	for si in timeSlotsList:
		for di in dayList:
			for rid in roomNumberList:
				tempScheduleMap[(si,di,rid)]=random.choice(courseList)
	fitness=calculateFitness(tempScheduleMap)
	globalScheduleMap[tempScheduleMap]=fitness

