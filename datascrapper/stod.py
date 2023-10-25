import numpy as np
# import BeautifulSoup4 as bsoup
from bs4 import BeautifulSoup
import requests

def get_text(elem):
    return None if elem is None else elem.text

 
page = requests.get('https://www.allsides.com/media-bias/media-bias-ratings') # Getting page HTML through request
soup = BeautifulSoup(page.content, 'html.parser') # Parsing content using beautifulsoup

print ( "Addi")
rows = soup.select('tbody tr')
row = rows[0]
#print(rows)
#name = rows.select('.views-field-title')
#print(name)
allsides_page = row.select_one('.views-field-title a')['href']
allsides_page = 'https://www.allsides.com' + allsides_page

print(allsides_page)


#print(name)
table =[]
for media in rows:
    source_name = media.select('.views-field-title')
    bias = media.select_one('.views-field-field-bias-image a')['href']
    # bias = bias.select('/media-bias/left-center')
    # print(type(bias))
    bias = bias.split('/')[-1]
    agree = row.select_one('.agree').text
    agree = int(agree)
    disagree = row.select_one('.disagree').text
    print(type(disagree))
    disagree = int(disagree)

    agree_ratio = agree / (disagree+agree)
    media.select_one('.community-feedback-rating-page')




  
    table.append({"SourceName":source_name,"Bias":bias,"Agree":agree,"Disagree":disagree,"Ratio":agree_ratio})
    print(f"Agree: {agree}, Disagree: {disagree}, Ratio {agree_ratio:.4f}")
print(table)

def get_agreeance_text(ratio):
    if ratio > 3: return "absolutely agrees"
    elif 2 < ratio <= 3: return "strongly agrees"
    elif 1.5 < ratio <= 2: return "agrees"
    elif 1 < ratio <= 1.5: return "somewhat agrees"
    elif ratio == 1: return "neutral"
    elif 0.67 < ratio < 1: return "somewhat disagrees"
    elif 0.5 < ratio <= 0.67: return "disagrees"
    elif 0.33 < ratio <= 0.5: return "strongly disagrees"
    elif ratio <= 0.33: return "absolutely disagrees"
    else: return None
print(get_agreeance_text(2.5))

