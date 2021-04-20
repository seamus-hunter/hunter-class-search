from PIL import Image
from selenium import webdriver
from selenium.webdriver.support.ui import Select

#start driver
def getInfo(subject, course):

  op = webdriver.FirefoxOptions()
  op.add_argument('--headless')
  op.add_argument(f'--window-size=1920,1080')
  #driver = webdriver.Chrome(options=op)
  driver = webdriver.Firefox(options=op)

  print('Navigating course directory...')

  #get the global search website
  driver.get('https://globalsearch.cuny.edu/')
  driver.implicitly_wait(10) #wait 10 seconds

  element = driver.find_element_by_css_selector('#HTR01') #Hunter College checkbox
  element.click()

  element = driver.find_element_by_css_selector('#t_pd > option:nth-child(2)') #upcoming term
  element.click()

  element = driver.find_element_by_css_selector('input.SSSBUTTON_CONFIRMLINK') #Next button
  element.click()

  driver.implicitly_wait(10) #wait 10 seconds

  #subject drop down
  select = Select(driver.find_element_by_id('subject_ld'))
  select.select_by_visible_text(str(subject))

  #course career drop down
  select = Select(driver.find_element_by_id('courseCareerId'))
  select.select_by_visible_text('Undergraduate')

  #uncheck the only show open classes box
  element = driver.find_element_by_css_selector('#open_classId')
  element.click()


  element = driver.find_element_by_css_selector('#btnGetAjax') #Search (Next) button
  element.click()

  driver.implicitly_wait(10) #wait 10 seconds

  print('Downloading class data from CUNY\'s server...')
  #reveal hunter classes
  element = driver.find_element_by_css_selector('#imageDivLink_inst0')
  element.click()

  #reveal class information (this section can be optimised)
  index = 0
  while index < 50:
    id = 'imageDivLink' + str(index)
    try:
      element = driver.find_element_by_id(id)
      element.click()
      index = index + 1
    except:
      break


  #store html data into log.txt
  element = driver.find_element_by_css_selector('html')
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
  element = driver.find_element_by_link_text(classNumber)
  element.click()

  driver.implicitly_wait(10) #wait 10 seconds
  #find full class details element
  element = driver.find_element_by_css_selector('#wrapper > form')

  #save screenshot
  S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
  driver.set_window_size(S('Width'),S('Height')) 
  driver.find_element_by_css_selector('#wrapper > form').screenshot(classNumber + '.png')


  #show image
  img = Image.open(classNumber + '.png')
  img.show(classNumber + '.png')

  driver.quit()

