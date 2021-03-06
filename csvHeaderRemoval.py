# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 18:50:28 2020
Removing Header from csv files.
@author: Rashmi

About the project:
Removes the header from all CSV files in the current working directory.
"""

import csv,os

os.mkdir('RemovedHeaderFiles')

# Loop through every file in the current working directory.
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue  #skip non-csv files
    print('Removing header from ',csvFilename,'...')
    
    #Read the CSV file in (skipping first row).
    csvrows = []
    file = open(csvFilename)
    r_object = csv.reader(file)
    for row in r_object:
        if r_object.line_num == 1:
            continue
        csvrows.append(row)
    file.close()
    
    #Write out the CSV file.
    file = open(os.path.join('RemovedHeaderFiles',csvFilename),'w',newline='')
    w_object = csv.writer(file)
    for row in csvrows:
        w_object.writerow(row)
    file.close()
