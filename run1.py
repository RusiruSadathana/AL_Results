import requests
import json
import csv
from requests.structures import CaseInsensitiveDict


token='1776016878:AAEWXP7zSt9abR7i-Ev_Y9L_fSd1U2nR-Ko'


def get_data(index_no,g):
    try:
        r=requests.get('https://www.doenets.lk/result/service/AlResult/'+str(index_no))
        jsondata = json.loads(r.text)

        if jsondata['year']==None:
            print(str(index_no)+' is not valid')
            
            
        else:

            
            year=str(jsondata['year'])
            name=jsondata['name']
            indexNo=str(jsondata['indexNo'])
            nic=str(jsondata['nic'])
            districtRank=str(jsondata['districtRank'])
            islandRank=str(jsondata['islandRank'])
            zScore=str(jsondata['zScore'])
            stream=jsondata['stream']
            Sub1name=jsondata['subjectResults'][0]['subjectName']
            Sub1result=jsondata['subjectResults'][0]['subjectResult']
            Sub2name=jsondata['subjectResults'][1]['subjectName']
            Sub2result=jsondata['subjectResults'][1]['subjectResult']
            Sub3name=jsondata['subjectResults'][2]['subjectName']
            Sub3result=jsondata['subjectResults'][2]['subjectResult']

            arr=[year,name,indexNo,nic,districtRank,islandRank,zScore,stream,Sub1name,Sub1result,Sub2name,Sub2result,Sub3name,Sub3result]
            print(indexNo)
            
            msg=year+'\n'+name+'\n'+indexNo+'\n'+nic+'\n'+districtRank+'\n'+islandRank+'\n'+zScore+'\n'+stream+'\n'+Sub1name+' '+Sub1result+'\n'+Sub2name+' '+Sub2result+'\n'+Sub3name+' '+Sub3result
            method='sendMessage'
            #response = requests.post(url='https://api.telegram.org/bot{0}/{1}'.format(token, method), data={'chat_id':-1001380999473, 'text': msg}).json() 

            with open('results_1.csv', 'a') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(arr)
                csvFile.close()
        
    except:
        print('err')

fromm=5000000  
to=7499999
g=1
for i in range(fromm,to):
	get_data(i,g)

#response = requests.post(url='https://api.telegram.org/bot{0}/{1}'.format(token, method),data={'chat_id':-1001380999473, 'text': 'Done start again'}).json()