#This program automates the CUNYfirst Global Search


from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

#user inputs course
course = input('Enter Course: ')
string = course.split()
prefix = string[0]
number = string[1]
flag = 0

if prefix.upper() == 'CSCI':
  subject = 'Computer Science'


browser = webdriver.Firefox()
print('Navigating course directory...')

#get the global search website
browser.get('https://globalsearch.cuny.edu/')
browser.implicitly_wait(10) #wait 10 seconds

element = browser.find_element_by_css_selector('#HTR01') #Hunter College checkbox
element.click()

element = browser.find_element_by_css_selector('#t_pd > option:nth-child(2)') #Fall 2021 Term
element.click()

element = browser.find_element_by_css_selector('input.SSSBUTTON_CONFIRMLINK') #Next button
element.click()

browser.implicitly_wait(10) #wait 10 seconds

#subject drop down
select = Select(browser.find_element_by_id('subject_ld'))
select.select_by_visible_text(str(subject))

#course career drop down
select = Select(browser.find_element_by_id('courseCareerId'))
select.select_by_visible_text('Undergraduate')

#uncheck the only show open classes box
element = browser.find_element_by_css_selector('#open_classId')
element.click()


element = browser.find_element_by_css_selector('#btnGetAjax') #Search (Next) button
element.click()

browser.implicitly_wait(10) #wait 10 seconds

print('Downloading class data from CUNY\'s server...')
#reveal hunter classes
element = browser.find_element_by_css_selector('#imageDivLink_inst0')
element.click()

#reveal class information
index = 0
while index < 50:
  id = 'imageDivLink' + str(index)
  try:
    element = browser.find_element_by_id(id)
    element.click()
    index = index + 1
  except:
    break
index = 0

#store html data into log.txt
element = browser.find_element_by_css_selector('html')
log = open('log.txt', 'w')
log.write(element.text)
log.close()

meetingInfo = {}

#see if course exists in log
log = open('log.txt', 'r')

for line in log:
  #print course
  if course.upper() in line:
    print(line.lstrip(' '))
    flag = 1

  #skip unnecessary lines
  elif flag == 1:
    flag = 2
  
  #print line and add class to dictionary, or end loop if blank
  elif flag == 2:
    if line != '\n':

      print(line)
      parts = line.split()
      meetingInfo[parts[0]] = line
      index = index + 1
      flag = 1
    else:
      log.close()
      break

#if course doesn't exist, end the program
if flag == 0:
  print(course.upper() + ' is not found.')
  exit()

#user enters class number
classNumber = input('Enter Class Number: ')

#goes to class page
element = browser.find_element_by_link_text(classNumber)
element.click()

browser.implicitly_wait(10) #wait 10 seconds

#store html data into log.txt
element = browser.find_element_by_css_selector('html')
log = open('log.txt', 'w')
log.write(element.text)
log.close()
browser.close()
print('\n')


string = meetingInfo[classNumber]
print(string)
parts = string.split()

#section
section = str(parts[1] + ' ' + parts[2])

#days and times
daystimes = str(parts[3] + ' ' + parts[4] + ' ' + parts[5] + ' ' + parts[6])

#room
if parts[7] == 'TBA':
  room = parts[7]
  instructor = parts[8]

log = open('log.txt', 'r')
contents = log.readlines()

#status
status = contents[8].lstrip(' ')

##print statements
print(contents[3])
print(contents[4])
print('Status: ' + status)
print('Class Number: ' + classNumber)
print('Section: ' + section)
print('Days & Times: ' + daystimes)
print('Instructor: ' + instructor)
print('Room: ' + room)
#print('Status: ' + status)
#print('Class Number: ' + classNumber)
#print('Session: ' + session)
#print('Units: ' + units)
#print('Instruction Mode: ' + instructionMode)
#print('Class Components: ' + classComponents)
#print('Career: ' + career)
#print('Dates: ' + dates)
#print('Grading: ' + grading)
#print('Location: ' + location)
#print('Campus: ' + campus)


#log.close()

