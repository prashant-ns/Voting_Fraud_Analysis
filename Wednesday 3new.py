import requests
from requests.auth import HTTPBasicAuth
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import time

from bs4 import BeautifulSoup

d = pd.read_csv('testfileNYFL.csv', delimiter = ',', names = ['Last_name','Title','Middle_name','First_Name','P','Address1','Address2','City','L_name','F_name','Q','Add1','Add2','City','R','S','Age'])
d.fillna("NA", inplace=True)

ds_ln = d['Last_name'].tolist()
ds_fn = d['First_Name'].tolist()
ds_mn = d['Middle_name'].tolist()
ds_age = d['Age'].tolist()
print(d.isnull().sum())

for i in range(0,10):
    scrape = []
    print('Scraping..', i,'instance at',time.strftime('%a %H:%M:%S'))
    for p in range(1,5):
        if ds_fn[i] == 'NA':
            URL = "https://www.spokeo.com/"+str(ds_mn[i])+"-"+str(ds_ln[i])+"/"+str(p)
            name = str(ds_mn[i]) + ' ' + str(ds_ln[i])
        else:
            URL = "https://www.spokeo.com/"+str(ds_fn[i])+"-"+str(ds_ln[i])+"/"+str(p)
            if ds_mn[i] == 'NA':
                name = str(ds_fn[i]) + ' ' + str(ds_ln[i])
            else:
                name = str(ds_fn[i]) + ' ' + str(ds_mn[i]) + ' ' + str(ds_ln[i])

        response = requests.get(URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        records = soup.findAll('div',attrs = {'class':'single-column-list-container'})
        new = soup.findAll('div',attrs = {'class':'top-xs item-info copy-2'})
        
        for record in records:
            list = []
            indicator = 0
            for data in records:
                a = record.div.text + ', '
                if name.lower() not in a.lower():
                    indicator = 1
                    break
                b = record.strong.text + ', '
                try:
                  c = record.span.text
                except AttributeError:
                  pass
                d = a+b+c
            if (indicator == 1):
                continue
            list.append(d)
            if list in scrape:
                break
            else:
                scrape.append(list)
    f = open('try.csv', 'a')
    for i in range(len(scrape)) :
        for j in range(len(scrape[i])) :
                   makeitastring = ''.join(map(str, scrape[i])).replace("(","")
                   makeitastring = ''.join(map(str, makeitastring)).replace(")","")
                   makeitastring = ''.join(map(str, makeitastring)).replace("'","")
                   f.write(makeitastring)
                   f.write('\n')
    f.close()


#d = pd.read_csv('testfileNYFL.csv', delimiter = ',', names = ['First_name','Title','Middle_name','Last_name','P','Address1','Address2','City','L_name','F_name','Q','Add1','Add2','City','R','S','Age'])

#colnames = ['First_name','Title','Middle_name','Last_name','P','Address1','Address2','City','L_name','F_name','Q','Add1','Add2','City','R','S','Age']

d = pd.read_csv('try.csv', delimiter = ',', names = ['First_name','Age','Location','Abbreviation','Location2','Location3','Location4','Location5']) 
d.to_csv('try.csv', index=False, encoding='utf-8')
data_new = pd.read_csv("try.csv")
data_new.fillna("NA", inplace=True)
new_name = data_new["First_name"].tolist()
new_age = data_new["Age"].tolist()
location_list = (data_new["Location"]+data_new["Abbreviation"]+data_new["Location2"]+data_new["Location3"]+data_new["Location4"]+data_new["Location5"]).tolist()

with open('fraud.csv', 'a') as ff:
    for i in range(0,10):
        if ds_fn[i] == 'NA':
            search_name = str(ds_mn[i]) + ' ' + str(ds_ln[i])
        elif ds_mn[i] == 'NA':
            search_name = str(ds_fn[i]) + ' ' + str(ds_ln[i])
        else:
            search_name = str(ds_fn[i]) + ' ' + str(ds_mn[i]) + ' ' + str(ds_ln[i])
        year = ds_age[i]
        for j in range(0,10):
            if((search_name.lower()) == (new_name[j].lower())):
                if 'NY' in location_list[j]:
                    if 'FL' in location_list[j]:
                        n_age = new_age[j].replace(' ','')
                        if n_age.isdigit():
                            if n_age == year or n_age == year+1 or n_age == year-1:
                                    ff.write(search_name)
                                    ff.write(',')
                                    ff.write(n_age)
                                    ff.write(',')
                                    ff.write(location_list[j])
                                    ff.write('\n')

d= pd.read_csv('fraud.csv', delimiter = ',', names = ['First_name','Age','Location'])
d.to_csv('fraud.csv', index=False, encoding='utf-8')





##                            break
##                    else:
##                        print(search_name + ' - ' +location_list[j])
                    



                    
##                    if new_age[j].isdigit():
##                        if new_age[j] == years:
##                    print(search_name + ' - ' +location_list[j])
##                            break
##                    else:
##                        print(search_name + ' - ' +location_list[j])
                              
    

##import csv
##t1 = open('testfileNYFL.csv', 'r')
##t2 = open('new.csv', 'r')
##fileone = t1.readlines()
##filetwo = t2.readlines()
##t1.close()
##t2.close()
##
##outFile = open('update.csv', 'w')
##x = 0
##for i in fileone:
##    if i == filetwo[x]:
##        outFile.write(filetwo[x])
##    x += 1
##outFile.close()
##data_ds = pd.DataFrame(d, columns = ['First_name','Title','Middle_name','Last_name','P','Address1','Address2','City','L_name','F_name','Q','Add1','Add2','City','R','S','Age'])

#ds_names = d['First_name'].tolist()
#print(ds_names[1])

##first_names_ds = data_ds.First_name.tolist()
##print(first_names_ds,end='\n')
   
#dFrame1 = pd.DataFrame(eval(makeitastring), columns=['Name','Age','City1','City2','City3','City4','City5','City6'])

##print(dFrame1)




    #to_csv('saksham_arora_AIT-580.csv', index=False, encoding='utf-8')
    #print(record.strong)
    #list.append(record.div + record.strong)



#print(list)


##    for x in scrape:
##        print(*x)
