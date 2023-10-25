import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

target_urls = [
    'https://www.realtor.com/realestateandhomes-search/Michigan',
    'https://www.realtor.com/realestateandhomes-search/Michigan?pg-2',
    'https://www.realtor.com/realestateandhomes-search/Michigan?pg-3'
]

for i in range(4,206):
   string = 'https://www.realtor.com/realestateandhomes-search/Michigan?pg=' + str(i)
   # print(string)
   target_urls.append(string)
# print( len(target_urls))
data=pd.DataFrame(columns=['Price','Broker','HouseStatus','Address','Bed','Bath','Spsqft','SizeAcre'])

for page in target_urls:
   head={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
   resp=requests.get(page,headers=head)
   soup = BeautifulSoup(resp.text, 'html.parser')
   allData = soup.find_all("div",{"class":"BasePropertyCard_propertyCardWrap__J0xUj"})
   #print(allData)
   
   for i in range(0, len(allData)):
      
      try:
         Price=allData[i].find("div",{"data-testid":"card-price"}).text
      except:
         Price=None
      try:
         Broker=allData[i].find("div",{"data-testid":"broker-title"}).text
      except:
         Broker=None
      try:
         House_status=allData[i].find("div",{"class":"base__StyledType-rui__sc-108xfm0-0 kpUjhd message"}).text
      except:
         House_status=None
      try:
         Address=allData[i].find("div",{"data-testid":"card-address"}).text
      except:
         Address=None
      metaData = allData[i].find("ul",{"class":"PropertyMetastyles__StyledPropertyMeta-rui__sc-1g5rdjn-0 KKDDp card-meta"})
      allMeta = metaData.find_all("li")
      for x in range(0, len(allMeta)):
         try:
            Bed=allMeta[0].text
         except:
            Bed=None
         try:
            Bath=allMeta[1].text
         except:
            Bath=None
         try:
            SizePerSqft=allMeta[2].text
         except:
            SizePerSqft=None
         try:
            SizeAcre=allMeta[3].text
         except:
            SizeAcre=None


      dat=pd.DataFrame({'Price':Price,'Broker':Broker,'HouseStatus':House_status,'Address':Address,'Bed':Bed,'Bath':Bath,'Spsqft':SizePerSqft,'SizeAcre':SizeAcre},index=[1])
      # dat={'Price':Price,'Broker':Broker,'HouseStatus':House_status,'Address':Address,'Bed':Bed,'Bath':Bath,'Spsqft':SizePerSqft,'SizeAcre':SizeAcre}
      data = pd.concat([data, dat], ignore_index=True)
   print(data)

data.to_csv('Housing_Price3.csv', index=False, sep=';')








