# -*- coding: utf-8 -*-
"""
Created on Wed May 20 09:13:01 2020

@author: sarad
"""

import re

fp = open('emailinventionstory.txt','r')

fp.seek(0)
text = fp.read()
print(text)
fp.close()

results = re.findall(r'email',text)
count = len(results)
print('Number of times email appeared: ', count)

citations = re.findall("\[[0-9]*\]", text)
print(citations)





