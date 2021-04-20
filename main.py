#This program automates the CUNYfirst Global Search

import crawl  # python script to navigate CUNY's Course directory
import prefixtosubject  # python script to convert the course prefix to the subject (needed to access course directory)


def main():
  #user inputs course
  course = input('Enter Course: ')
  string = course.split()
  number = string[1]

  #get the subject from the prefix
  subject = prefixtosubject.findSubject(string[0].upper())

  print('Starting driver...')
  crawl.getInfo(subject, course.upper())

if __name__ == '__main__':
  main()
