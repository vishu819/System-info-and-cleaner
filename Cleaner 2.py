from os import *
import matplotlib.pyplot as p
import re

directory = raw_input("Enter Directory")
chdir(directory)
addresses={}
Extentions = []
count=0
count_pictures,count_video,count_audio,count_others=0,0,0,0

#WALK WALA LOOP
for root, dirs, files in walk(directory):
    #FILES  WALA  LOOP
    for i in files:
        ########################TO COUNT PICTURES,,VIDEO,OTHERS###################################
        if i.lower().endswith('.jpg') or i.lower().endswith('.jpeg') or i.lower().endswith('.png') or i.lower().endswith('tif') or i.lower().endswith('gif'):
            count_pictures+=1

        elif i.lower().endswith('.mkv')or i.lower().endswith('.wmv') or i.lower().endswith('.mp4')or i.lower().endswith('m4v') or i.lower().endswith('.avi') or i.lower().endswith('.flv') or i.lower().endswith('.vob') or i.lower().endswith('.mov') or i.lower().endswith('.3gp') or i.lower().endswith('.mpeg') or i.lower().endswith('.mpg'):
            count_video+=1

        elif i.lower().endswith('.mp3') or i.lower().endswith('.wav') or i.lower().endswith('.aac') or i.lower().endswith('.wma') or i.lower().endswith('.flac') or i.lower().endswith('.raw')or i.lower().endswith('.m4a') or i.lower().endswith('.m4b'):
            count_audio+=1

        else:
            count_others+=1
        ###########################################################################################

        match = re.search('\.[a-zA-Z3-4]+$', i)#To filter some uncommon extentions and reduce dict

        if match:
            addresses[root+'\\'+i]=0  #Dictionary me addresses of all files and 0 common value

            if match.group().lower() not in Extentions:
                Extentions.append(match.group().lower())#For Extention List

###############For GRAPH#############################################
labels1=('Pictures','Audio','Video','Others')
explode=(0.0, 0.05, 0.00, 0.02)
sizes1=(count_pictures,count_audio,count_video,count_others)
p.pie(sizes1,labels=labels1,autopct='%.2f%%',explode=explode)
p.show()
######################################################################

print'Extentions are-->',Extentions
print'=='*70
WhichExtention=raw_input('Which Extention Files to search')
WhichExtention='\\'+WhichExtention

WantShowFiles=raw_input('Want to show Files ---Press Y for Yes or N for No')
for i in addresses.keys():
    match = re.search(WhichExtention, i)
    if match:
        count += 1
        if WantShowFiles=='Y':
            print i.rsplit("\\")[-1] #to show the files of particular extention
print
print '=='*70
print 'Count of Extention is-->> %r'%(count)
input()
#used to for deletion further
'''dictToDel={} 
for k, v in addresses.iteritems():
    dictToDel.setdefault(v, []).append(k)'''




