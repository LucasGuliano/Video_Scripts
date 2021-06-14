#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 10:25:54 2020

@author: lguliano
"""
#   Data is grabbed from https://sdo.gsfc.nasa.gov/assets/img/dailymov/

import os
from datetime import date,datetime
from datetime import timedelta as dt
import numpy as np
import subprocess

#          Set wavelength and  parameters below     
      
#Select the 9 wavelengths that will be made into the 9-quadrant movie
#wave_set = ['0094','0131', '0171', '0211', '0304', '1700', 'HMIIF', 'HMIBC', 'HMIIC']
wave_set = ['0094','0131', '0171', '0211', '0193', '0304', '0335', '1600', '1700']

user_input = True
#user_input = False

###########  Start time and span  #################
if user_input == True:
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

        sday = datetime(start_year, start_month, start_day, 0, 0, 0)
        eday = datetime(end_year, end_month, end_day, 0, 0, 0)

if user_input == False:
        eday = datetime.utcnow()

        span = 7 #Span of days that the movie will cover
        sday = eday-dt(days=span)

        sday = datetime(2021, 05, 7, 12, 0, 0, 0)
        eday = datetime(2021, 05, 8, 0, 0, 0, 0)

########################################################################################

##########################################################
# Make sure folders exist for each wavelength            #
##########################################################
#Make directories if not there
try:
	os.mkdir('STEREO')
	os.mkdir('Nine_Quadrant_Movies')
except OSError:
    print('Creating Nine Quadrant Movie')

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
Nine_Movies_Command = '' 
for wave in wave_set:
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
            #new_vid_com=new_vid_com+'wget https://sdo.gsfc.nasa.gov/assets/img/dailymov/'+YYYY+'/'+MM+'/'+DD+'/'+dayt+'_1024_'+wave+'.mp4'+'\n'
    
    #Create command to make movie out of the data (writes all files in folder to txt file then merges with ffmpeg)
    make_movie_com ='rm *.txt'+'\n'+'find *.mp4 >> temp.txt'+'\n'+'foreach v (`cat temp.txt`)'+'\n'+'echo file $v >> file_list.txt'+'\n'+'end'+'\n'+'ffmpeg -nostdin -f concat -safe 0 -i file_list.txt ../Nine_Quadrant_Movies/'+wave+'.mp4'+'\n'+'rm *.txt'+'\n'+'cd ../'       
            
    #Create command to remove old movie, add new files, and create new movie
    New_Command = '\n'+'cd '+wave +'\n'+ new_vid_com + make_movie_com +'\n' 
    Nine_Movies_Command = Nine_Movies_Command+New_Command     


#####################################################
#           Stero Videos     #
#####################################################

days = movie_days[(len(movie_days)-4):-1]
stereo_download = ''
for dayt in days:
    data_link = 'python -c '+'"import wget; wget.download('+"'https://stereo-ssc.nascom.nasa.gov/browse/"+str(dayt.year)+'/'+str(dayt.month).zfill(2)+'/'+str(dayt.day).zfill(2)+'/ahead_'+str(dayt.year)+str(dayt.month).zfill(2)+str(dayt.day).zfill(2)+"_euvi_195_512.mpg')"+'"'+'\n'
    stereo_download = stereo_download + data_link

#Rest of the stereo movie command
stereo_movie_instructions = 'set ddate='+date_array[-1]+'\n'+'rm *.txt'+'\n'+'find *.mpg >> temp.txt'+'\n'+'foreach v (`cat temp.txt`)'+'\n'+'echo file $v >> mag_file_list.txt'+'\n'+'end'+'\n'+'ffmpeg -nostdin -f concat -safe 0 -i mag_file_list.txt STEREO_Far_Side.mp4'+'\n'+'ffmpeg -nostdin -i STEREO_Far_Side.mp4 -filter:v "setpts=0.5*PTS" STEREO_Far_Side.mp4_${ddate}.mp4'+'\n'+'rm *.txt'+'\n'    

#####################################################
#           Build the 9-quad make movie command     #
#####################################################
NQ_ls_Command = '\n'+'cd Nine_Quadrant_Movies'+'\n'+'ffmpeg -i '+wave_set[0]+'.mp4 -i '+wave_set[1]+'.mp4 -i '+wave_set[2]+'.mp4 -i '+wave_set[3]+'.mp4 -i '+wave_set[4]+'.mp4 -i '+wave_set[5]+'.mp4 -i '+wave_set[6]+'.mp4 -i '+wave_set[7]+'.mp4 -i '+wave_set[8]+'.mp4 '
NQ_Scale_Command ='-filter_complex "color=s=3200x1800:c=black [base];[0:v] setpts=PTS-STARTPTS, scale=600x600 [a];[1:v] setpts=PTS-STARTPTS, scale=600x600 [b];[2:v] setpts=PTS-STARTPTS, scale=600x600 [c];[3:v] setpts=PTS-STARTPTS, scale=600x600 [d];[4:v] setpts=PTS-STARTPTS, scale=600x600 [e];[5:v] setpts=PTS-STARTPTS, scale=600x600 [f];[6:v] setpts=PTS-STARTPTS, scale=550x550 [g];[7:v] setpts=PTS-STARTPTS, scale=550x550 [h];[8:v] setpts=PTS-STARTPTS, scale=550x550 [i];'
NQ_Overlay_Command='[base][a] overlay=shortest=1:x=233[tmp1];[tmp1][b] overlay=shortest=1:x=1300[tmp2];[tmp2][c] overlay=shortest=1:x=2368[tmp3];[tmp3][d] overlay=shortest=1:x=233:y=600[tmp4];[tmp4][e] overlay=shortest=1:x=1300:y=600[tmp5];[tmp5][f] overlay=shortest=1:x=2368:y=600[tmp6];[tmp6][g] overlay=shortest=1:x=233:y=1250[tmp7];[tmp7][h] overlay=shortest=1:x=1300:y=1250[tmp8];[tmp8][i] overlay=shortest=1:x=2368:y=1250" -y Nine_Quadrant_Video.mp4'  
Make_NQ = NQ_ls_Command+NQ_Scale_Command+NQ_Overlay_Command
#Move_Display = '\n'+'cp Nine_Quadrant_Video.mp4 ../../VIDEO_WALL_DISPLAY/Nine_Quadrant_Video.mp4'+'\n' 
Move_Display = ''
#####################################################
#    Write and Exucute all the built commands       #
#####################################################
#Write all instructions to .csh file that the user can exucute 
com = open('Nine_Quadrant_Command.csh','w')
com.write('#!/bin/tcsh'+'\n'+'cd STEREO\n'+'rm *'+'\n'+stereo_download+stereo_movie_instructions+'\n'+'cd ..'+'\n'+'rm Nine_Quadrant_Movies/*'+ Nine_Movies_Command+'\n'+Make_NQ+Move_Display+'#end')
com.close()

#change file to executable
mod = subprocess.call(['/bin/csh','-c','chmod a+x Nine_Quadrant_Command.csh'])

#run ffmpeg
run = subprocess.call(['/bin/csh','-c','./Nine_Quadrant_Command.csh'])
