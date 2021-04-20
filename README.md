# Hunter Class Search

Hunter Class Search can tell you information about a class of your choice in Hunter College. The program saves an image of the class details.

It can show:
- Class Status
- Days and Times
- Room
- Location
- Instructor
- Enrollment Requirements
- Class Attributes
- Class Capacity
- Waitlist Capacity
- Course Description



## Installation
Hunter Class Search runs on Python 3.9. It can be downloaded [here](https://www.python.org/downloads/).

In addition, the Selenium and Pillow libraries are used.
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install them.

```bash
pip install selenium pillow
```
You will also need to install Firefox and geckodriver. Firefox can be downloaded [here](https://www.mozilla.org/firefox) and geckodriver can be downloaded [here](https://github.com/mozilla/geckodriver/releases) (extract the file and move it to the location you installed Python).

## Usage
This program is meant to  run on the command line (*Command Prompt* on Windows or *Terminal* on macOS). If the files are installed in the current working directory, type the following in the command line:

```bash
python main.py
```
If the files are installed in a different directory, you can type the path to main.py:

```bash
python /Users/myself/.../main.py
```
Once you get the program running, you will be asked to enter the course you are looking for in the format of [prefix][number].

Example:

```
Enter course: CSCI 23200
```
You then have to wait a few seconds for the program to gather the data.
```
CSCI 23200 - Rel Databases & SQL Programg

10729 01-LEC Regular MoWe 5:35PM - 6:50PM  TBA  Lam,Alvin  Online  08/25/2021 - 12/21/2021 
12422 02-LEC Regular TuFr 9:45AM - 11:00AM  TBA  Avshalumov,Ariel  Online  08/25/2021 - 12/21/2021
13397 03-LEC Regular TuTh 5:35PM - 6:50PM  TBA  TBA  Online  08/25/2021 - 12/21/2021

Enter Class Number: 13397
```
An image will then be created and opened containing all the class details


## License
[GNU Affero General Public License v3.0](https://choosealicense.com/licenses/agpl-3.0/)
