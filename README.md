# Easy Grading
Automatically enter grades into edoz.

## Requirements
Download chromedriver from [the Chromium website](https://sites.google.com/a/chromium.org/chromedriver/downloads) and add it to the PATH. For example:
```
wget https://chromedriver.storage.googleapis.com/2.27/chromedriver_mac64.zip
unzip chromedriver_mac64.zip
PATH=$PATH:.
```

Install selenium
```
pip install selenium
```

## Running
Start the script with the path to chromedriver and to your grade CSV file with (student it, grade) pairs, one per line.
```
python enter_edoz_grades.py -c chromedriver -g grades.csv
```
