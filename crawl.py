from selenium import webdriver
from selenium.webdriver.support.ui import Select
from PIL import Image

#start browser
def getInfo(subject, course):
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

  #reveal class information (this section can be optimised)
  index = 0
  while index < 50:
    id = 'imageDivLink' + str(index)
    try:
      element = browser.find_element_by_id(id)
      element.click()
      index = index + 1
    except:
      break


  #store html data into log.txt
  element = browser.find_element_by_css_selector('html')
  log = open('log.txt', 'w')
  log.write(element.text)
  log.close()

  #see if course exists in log
  log = open('log.txt', 'r')


  
  #FLAGS
  #flag 0 - course not found
  #flag 1 - next line is unnecessary
  #flag 2 - next line is either blank (in which case, end loop) or is class info

  flag = 0
  for line in log:
    #print course
    if course in line:
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
        #meetingInfo[parts[0]] = line
        #index = index + 1
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
  #find full class details element
  element = browser.find_element_by_css_selector('#wrapper > form')
  location = element.location
  size = element.size
  #save screenshot
  browser.save_screenshot(classNumber + '.png')
  #crop image
  x = location['x']
  y = location['y']
  width = location['x'] + size['width']
  height = location['y'] + size['height']
  img = Image.open(classNumber + '.png')
  img = img.crop((int(x), int(y), int(width), int(height)))
  img.save(classNumber + '.png')

  #show image
  img.show(classNumber + '.png')

  browser.quit()

  '''
  #store html data into log.txt
  element = browser.find_element_by_css_selector('html')
  log = open('log.txt', 'w')
  log.write(element.text)
  log.close()
  browser.close()
  print('\n')
  '''
