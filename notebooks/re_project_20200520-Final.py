# -*- coding: utf-8 -*-
"""
Created on Wed May 20 09:15:14 2020

@author: sarad
"""

#Project Assignment: Extracting email ids from a text document

import re

fp1 = open('sampleemailtext.txt','r')
emailtext = fp1.read()
print(emailtext)
fp1.close()

#You have to write a regular expression to extract all types of email ids from the above text

# TO DO: Write a regular expression to find email ids of any kind
email_pattern = 

#Extract the email ids based on your regular expression and display those list of extracted email ids

emails = re.findall(email_pattern, emailtext)
print(emails)


