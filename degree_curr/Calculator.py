from __future__ import unicode_literals
from frappe import utils
from datetime import date
import frappe, json
from datetime import timedelta

def calculate(doc, method):
	frappe.msgprint("hook working.. Student no is:{} \n Student:{}".format(doc.student_number,doc.student_name))

def test1(a,b):
	frappe.msgprint("hook working.. Student no is") #doc n method argz

@frappe.whitelist(allow_guest=True)
def test(student_number):
	line = "Yes, js hook working in py{}".format(student_number)

	doc_a = frappe.get_doc("Student",student_number)
	list1 = []
	for t in doc_a.get("courses_passed"): #Create a list of a list... clever me
		#frappe.msgprint(t.course)
		list1.append(t.course)
	#meetRequesites(student_number)
	TEST_1=course_checker(student_number)#get_prereq("MAM1021")
	return TEST_1


def get_passed(student_number):
	doc_a = frappe.get_doc("Student",student_number)
	list1 = []
	for t in doc_a.get("courses_passed"): #Create a list of a list... clever me
		list1.append(t.course)
	return list1

def get_remaining(student_number):
	doc_a = frappe.get_doc("Student",student_number)
	list1 = []
	for t in doc_a.get("courses_remaining"): #Create a list of a list... clever me
		list1.append(t.course)
	return list1

def get_prereq(course):
	doc_a = frappe.get_doc("Course",course)
	list1 = []
	for t in doc_a.get("prerequisites"): #Create a list of a list... clever me
		list1.append(t.course)
	return list1

def get_core(course):
	doc_a = frappe.get_doc("Course",course)
	list1 = []
	for t in doc_a.get("core_requisites"): #Create a list of a list... clever me
		list1.append(t.course)
	return list1

#Comparing prereq of ea remaining course to ea passed course
def get_possible(remaining, passed):
	for i in remaining:
		pre = get_prereq(i) #list of prereq
		possible=[]
		for j in pre:
			if j in passed:
				if i not in possible:
					possible.append(i)
	return possible


def course_checker(student_number):
	remaining= get_remaining(student_number)
	passed = get_passed(student_number)
	possible= get_possible(remaining,passed)
	return possible