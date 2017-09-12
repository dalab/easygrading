# Easy Grading
Automatically enter grades into edoz.

## Setup
Clone the repo, download chromedriver from [the Chromium website](https://sites.google.com/a/chromium.org/chromedriver/downloads), temporarily add it to the PATH, and install selenium. For example:
```
git clone git@github.com:dalab/easygrading.git
cd easygrading
wget https://chromedriver.storage.googleapis.com/2.27/chromedriver_mac64.zip
unzip chromedriver_mac64.zip
PATH=$PATH:.
pip install selenium
```

## Running
Start the script with the path to chromedriver and to your grade CSV file with (student id, grade) pairs, one per line.
```
python enter_edoz_grades.py -c chromedriver -g grades.csv
```
