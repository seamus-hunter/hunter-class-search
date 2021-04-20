#This program automates the CUNYfirst Global Search

import prefixtosubject
import crawl

#user inputs course
course = input('Enter Course: ')
string = course.split()
number = string[1]
flag = 0

#get the subject from the prefix
subject = prefixtosubject.findSubject(string[0].upper())

crawl.getInfo(subject, course.upper())
