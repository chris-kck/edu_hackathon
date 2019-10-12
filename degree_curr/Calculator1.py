def main():
	

	student = frappe.get_doc(doctype, name) 
	#Student("tatenda", "mgdtat002" ["1", "2" , "3", "4", "6"], ["7", "8" , "9", "10", "11"])

	coursesPassed = student.cousesPassed
	remainingCourses = student.remainingCourses
	
	
	for x in remainingCourses:
  		meetRequesites(x) #now we have a list of courses not done and prerequisits are met


def get_courses_list(doc):
	frappe.get_doc("Student",doc.student_number)
	list1 = []
	for t in doc_a.get("courses_passed"): #Create a list of a list... clever me
		list1.append({	'course':t.course,
        			})
	return list1

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






