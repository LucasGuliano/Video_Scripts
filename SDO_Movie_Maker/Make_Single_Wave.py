#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 10:25:54 2020

@author: lguliano
"""
#   Data is grabbed from https://sdo.gsfc.nasa.gov/assets/img/dailymov/

import os
from datetime import datetime
from datetime import timedelta as dt
import numpy as np
import subprocess

#Take in user input for wavelength and date range to be made

print("Enter one of the following wavelengths for the movie:")
print("0094, 0131, 0171, 0193, 0211, 0304, 0335, 1600, 1700")
print("HMIB, HMIBC, HMID, HMII, HMIIC, HMIIF")
wave = raw_input()

print("Enter the starting date in the form of YYYYMMDD:")
start_date = raw_input()
print("Enter the end date in the form of YYYYMMDD:")
end_date = raw_input()

start_year= int(start_date[0:4])
start_month= int(start_date[4:6])
start_day= int(start_date[6:8])
end_year= int(end_date[0:4])
end_month= int(end_date[4:6])
end_day= int(end_date[6:8])


###########  Start time and span  #################
sday = datetime(start_year, start_month, start_day, 0, 0, 0, 0)
eday = datetime(end_year, end_month, end_day, 0, 0, 0, 0)

#Make folder to store all movies that are made
try:
	os.mkdir('Single_Wave_Movies')
except OSError:
    print('Single_Wave_Movies')

########################################################################################

##########################################################
# Create array of YYYYMMDD that the movies will cover    #
##########################################################
movie_days =  np.arange(sday,eday,dt(days=1)).astype(datetime)
date_array = []
for i in movie_days:
    YYYYMMDD = i.date().strftime('%Y%m%d')
    date_array.append(YYYYMMDD)

#######################################################################
####        Build command to get the the 9-quadrant movies   ##########
#######################################################################
Movies_Command = '' 
work_dir=wave
#Check if folder already exists for that wavelength
if not os.path.isdir(work_dir):
    os.mkdir(work_dir)
if os.path.isfile(work_dir+'/*.txt'):
    os.remove(work_dir+'/*.txt')
file_list = os.listdir(work_dir)
#Check to remove old files as long as folder isn't empty
if file_list:
    for f in file_list:
        if f[0:8] not in date_array and f[0] != '.':
            os.remove(work_dir+'/'+f)

#Determine which files need to be downloaded
file_YYYYMMDD_list = []
file_list = os.listdir(work_dir)
for i in file_list:
    if i[0] != '.':
        file_YYYYMMDD_list.append(i[0:8])
        
#create string command that will download all new data
new_vid_com = ''
for dayt in date_array:
    if dayt not in file_YYYYMMDD_list:
        YYYY = dayt[0:4]
        MM = dayt[4:6]
        DD = dayt[6:8]
        new_vid_com=new_vid_com+'python -c '+'"import wget; wget.download('+"'https://sdo.gsfc.nasa.gov/assets/img/dailymov/"+YYYY+'/'+MM+'/'+DD+'/'+dayt+'_1024_'+wave+".mp4')"+'"'+'\n'

#Create command to make movie out of the data (writes all files in folder to txt file then merges with ffmpeg)
make_movie_com ='rm *.txt'+'\n'+'find *.mp4 >> temp.txt'+'\n'+'foreach v (`cat temp.txt`)'+'\n'+'echo file $v >> file_list.txt'+'\n'+'end'+'\n'+'ffmpeg -nostdin -f concat -safe 0 -i file_list.txt '+wave+'_'+start_date+'_to_'+end_date+'.mp4'+'\n'+'rm *.txt'+'\n'       
        
#Create command to remove old movie, add new files, and create new movie, and move to movie folder
New_Command = '\n'+'cd '+wave +'\n'+ new_vid_com + make_movie_com +'\n'+'mv '+wave+'_'+start_date+'_to_'+end_date+'.mp4'+' ../Single_Wave_Movies'+'\n'+'cd ../'+'\n'+'rm -R '+work_dir
Movies_Command = Movies_Command+New_Command     



#    Write and Exucute all the built commands       #
#####################################################
#Write all instructions to .csh file that the user can exucute 
com = open('Single_Wave_Command.csh','w')
com.write('#!/bin/tcsh'+'\n'+ Movies_Command+'\n'+'#end')
com.close()

#change file to executable
mod = subprocess.call(['/bin/csh','-c','chmod a+x Single_Wave_Command.csh'])

#run ffmpeg
run = subprocess.call(['/bin/csh','-c','./Single_Wave_Command.csh'])
