# -*- coding: utf-8 -*-
"""
Created on Thu May  7 13:03:36 2020

@author: Shivam Bhatnagar
"""

from bs4 import BeautifulSoup as bs
import requests

url = r'https://www.bbc.co.uk/'

data = requests.get(url)

soup = bs(data.text, 'html.parser')

title = soup.title.string

print(f'The webpage is {title}')