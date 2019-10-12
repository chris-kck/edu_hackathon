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
def test(test):
	line = "Yes, js hook working{}".format(test)
	return line