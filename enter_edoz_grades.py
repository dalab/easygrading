"""
Enter grades into edoz.
"""

from __future__ import print_function
import sys
import argparse
from selenium import webdriver

# constants
EDOZ_URL='https://www.lehrbetrieb.ethz.ch/edoz/loginPre.do?lang=en'

# parameters
parser = argparse.ArgumentParser(description="Enter grades into edoz.")
parser.add_argument("-c", "--chromedriver", required=True,
    help="Chromedriver executable (download from https://sites.google.com/a/chromium.org/chromedriver/downloads).")
parser.add_argument("-g", "--grades", required=True,
    help="Path to CSV file containing (student id, grade) pairs.")
args = parser.parse_args(sys.argv[1:])

# Read grades
grades = {}
with open(args.grades, 'r') as reader:
    for line in reader:
        sep = ',' if ',' in line else None
        split = line.strip().split(sep)
        if len(split) == 2:
            student_id = split[0].strip()
            grade = split[1].strip()
            grades[student_id] = grade
print("Read grades of %d students." % len(grades))

# Open edoz homepage in selenium-accessible browser
driver = webdriver.Chrome(args.chromedriver)
driver.get(EDOZ_URL)

# Replace Python 2 input with raw_input
try:
    input = raw_input
except NameError:
    pass

print("Please login to edoz and navigate to the grades page.")
input("Then press enter to continue.")

# Fill in the grades
table = driver.find_element_by_xpath("//table[@class='tablelist']")
rows = driver.find_elements_by_tag_name('tr')
for row in rows:
    cells = row.find_elements_by_tag_name('td')
    if len(cells) > 8:
        student_id = cells[2].text.strip()
        if student_id in grades:
            grade_field = cells[8].find_element_by_tag_name('input')
            grade_field.send_keys(grades[student_id])
            # If you want to delete all of the grades, uncomment the following:
            # from selenium.webdriver.common.keys import Keys
            # for _ in range(4):
            #     grade_field.send_keys(Keys.BACKSPACE)

# Press save
driver.find_element_by_name('buttons.save.name').click()
