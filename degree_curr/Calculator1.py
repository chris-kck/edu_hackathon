def main():
	

	student = Student("tatenda", "mgdtat002" ["1", "2" , "3", "4", "6"], ["7", "8" , "9", "10", "11"])

	coursesPassed = student.cousesPassed 

	remainingCourses = student.remainingCourses
	posibble = []
	
	for x in remainingCourses:
  		meetRequesites(x) #now we have a list of courses not done and prerequisits are met








def meetRequesites(course):
	for x in course.preRequisites:
		if x not in coursesPassed:
			pass
		else:
		possible.append(course)


			return True
	#loop in courses done looking for course.requisites
	#return array of doable couses

def checkClashes(possibleCombination[]):
	for x in range (0, len(possibleCombination):
		temp = possibleCombination[x]
		for i in range (0, len(possibleCombination):
			if temp.timeOffered == i.timeOffered






