import requests
from requests.auth import HTTPBasicAuth
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

from bs4 import BeautifulSoup


d = pd.read_csv('testfileNYFL.csv', delimiter = ',', names = ['Last_name','Title','Middle_name','First_Name','P','Address1','Address2','City','L_name','F_name','Q','Add1','Add2','City','R','S','Age'])

ds_ln = d['Last_name'].tolist()
ds_fn = d['First_Name'].tolist()\

for i in range(1504,1512):
    URL = "https://www.spokeo.com/"+ds_fn[i]+'-'+ds_ln[i]+"?loaded=1"
    print(URL)
    response = requests.get(URL)
 #  print(response)
    soup = BeautifulSoup(response.text, 'html.parser')
    records = soup.findAll('div',attrs = {'class':'single-column-list-container'})
    new = soup.findAll('div',attrs = {'class':'top-xs item-info copy-2'})
    scrape = []
    for record in records:
        list = []
        for data in records:
            a = record.div.text
            b = record.strong.text
            c = record.span.text
            d = a,b,c
##            print("CCCCC=",c)
        list.append(d)
 #       print("List is",list)
        print(list)
        scrape.append(list)
#       print(scrape)
##        with open('try.csv', 'w') as f:
##            for i in range(len(scrape)) :
##                for j in range(len(scrape[i])) :
##                    makeitastring = ''.join(map(str, scrape[i])).replace("(","")
##                    makeitastring = ''.join(map(str, makeitastring)).replace(")","")
##                    makeitastring = ''.join(map(str, makeitastring)).replace("'","")
##                    f.write(makeitastring)
##                    f.write('\n')



#colnames = ['First_name','Title','Middle_name','Last_name','P','Address1','Address2','City','L_name','F_name','Q','Add1','Add2','City','R','S','Age']

#d = pd.read_csv('testfileNYFL.csv', delimiter = ',', names = ['First_name','Title','Middle_name','Last_name','P','Address1','Address2','City','L_name','F_name','Q','Add1','Add2','City','R','S','Age'])

##data_ds = pd.DataFrame(d, columns = ['First_name','Title','Middle_name','Last_name','P','Address1','Address2','City','L_name','F_name','Q','Add1','Add2','City','R','S','Age'])

#ds_names = d['First_name'].tolist()
#print(ds_names[1])

##first_names_ds = data_ds.First_name.tolist()
##print(first_names_ds,end='\n')
   
#dFrame1 = pd.DataFrame(eval(makeitastring), columns=['Name','Age','City1','City2','City3','City4','City5','City6'])

##print(dFrame1)


#makeitastring.to_csv('try.txt', index=False, encoding='utf-8')

    #to_csv('saksham_arora_AIT-580.csv', index=False, encoding='utf-8')
    #print(record.strong)
    #list.append(record.div + record.strong)



#print(list)
