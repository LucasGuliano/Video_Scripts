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

###########  Start time and span  #################
wave = 'HMIBC'
eday = datetime.utcnow()

span = 30 #Span of days that the movie will cover
sday = eday-dt(days=span)

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
####        Build com ##########
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
        new_vid_com=new_vid_com+'wget --no-check-certificate https://sdo.gsfc.nasa.gov/assets/img/dailymov/'+YYYY+'/'+MM+'/'+DD+'/'+dayt+'_1024_'+wave+'.mp4'+'\n'

#Create command to make movie out of the data (writes all files in folder to txt file then merges with ffmpeg)
make_movie_com ='rm *.txt'+'\n'+'find *.mp4 >> temp.txt'+'\n'+'foreach v (`cat temp.txt`)'+'\n'+'echo file $v >> file_list.txt'+'\n'+'end'+'\n'+'ffmpeg -nostdin -f concat -safe 0 -i file_list.txt '+wave+'.mp4'+'\n'+'rm *.txt'+'\n'       

size_command = '\n'+'ffmpeg -i HMIBC.mp4 -vf "scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2" Magnetic_Month.mp4'
   
    
#Create command to remove old movie, add new files, and create new movie, and move to movie folder
New_Command = '\n'+'cd '+wave +'\n'+ new_vid_com + make_movie_com + size_command+'\n'+'mv '+'Magnetic_Month.mp4'+' ../../VIDEO_WALL_DISPLAY'+'\n'+'cd ../'+'\n'+'rm -R '+work_dir
Movies_Command = Movies_Command+New_Command




#    Write and Exucute all the built commands       #
#####################################################
#Write all instructions to .csh file that the user can exucute 
com = open('Magnetic_Command.csh','w')
com.write('#!/bin/tcsh'+'\n'+ Movies_Command+'\n'+'#end')
com.close()

#change file to executable
mod = subprocess.call(['/bin/csh','-c','chmod a+x Magnetic_Command.csh'])

#run ffmpeg
run = subprocess.call(['/bin/csh','-c','./Magnetic_Command.csh'])
