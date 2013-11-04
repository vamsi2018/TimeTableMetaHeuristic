import sys
from sys import argv

##timeTableSchedule
def calculateFitness(timeTableSchedule1):
	inv_timetableSchedule = {}
	roomSet = []
	daySet = []
	tempList = []
	conflict = 0
	for k, v in timeTableSchedule1.iteritems():
		inv_timetableSchedule[v] = inv_timetableSchedule.get(v,[])
		inv_timetableSchedule[v].append(k)
	
	for cid in inv_timetableSchedule.keys():
		tempList = inv_timetableSchedule[cid]
		if len(tempList) > 1:
			conflict = conflict + 1
	tempMap = {}
	for (m,n,o) in timeTableSchedule1.keys():
		tempMap.setdefault((m,n),[])
		tempMap[(m,n)] += [timeTableSchedule1[(m,n,o)]]
	
	for (m,n) in tempMap.keys():
        conflict += FacultyAndRoomConflicts(tempMap[(m,n)])

	fitness = 1.0
	fitness = (1 / (1 + conflict))
	return fitness
	

def FacultyAndRoomConflict(cList):
	roomSet = []
	facultySet = []
	studentSet = []
#	cList = []
#	for (k,l) in course_student_map.keys():
#		cList += [tempMap[(k,l)]]
	for cid in cList:
		facultySet += [set(courseFacultyListMap[cid])]		
		studentSet += [set(studentListMap[cid])]			
# 	return isNotIntersection(roomSet) & isNotIntersection(facultySet) & isNotIntersection(studentSet)
 	return isNotIntersection(studentSet) + isNotIntersection(facultySet)

def isNotIntersection(someSet):
	conflicts = 0
	for i in range(len(someSet)):
		for j in range(i+1,len(someSet)):
			if (someSet[i] & someSet[j]) != set([]):
				conflicts = conflicts + 1 
	return conflicts

