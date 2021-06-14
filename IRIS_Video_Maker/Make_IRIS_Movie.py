#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 12:18:49 2020

@author: lguliano
"""
###########################################################################################
#
# To run this script, the folder in the same directory called IRIS_Movies must exist
# Add movies from the https://www.lmsal.com/hek/hcr?cmd=view-recent-events&instrument=iris
# All movies in this folder will be merged to a single video for the video wall
#
###########################################################################################

import os
import subprocess

#Make directories if not there
try:
    os.mkdir('IRIS_Movies')
    os.mkdir('IRIS_Movies/Reformatted')
except OSError:
    print('Creating IRIS Movie')

###############################################
#Get list of mp4 files in movie directory
###############################################
cwd = os.getcwd()
movie_dir = cwd+'/IRIS_Movies'
os.chdir(movie_dir)

#Make list of all .mp4 files
filelist = os.listdir(movie_dir)
movielist = [m for m in filelist if ".mp4" in m]

#Set up commands to be written to exucutable
reformat_com = ''
merge_com = '\n'+'cd Reformatted\n'+'find *.mp4 >> temp.txt\n'+'foreach v ( `cat temp.txt` )\n'+'echo file $v >> IRIS_file_list.txt\n'+'end\n'+'ffmpeg -nostdin -f concat -safe 0 -i IRIS_file_list.txt -y IRIS_Highlight_Video.mp4\n'
move_com = '\n'+'cp IRIS_Highlight_Video.mp4 ../../../VIDEO_WALL_DISPLAY\n'+'mv IRIS_Highlight_Video.mp4 ../../\n'+'rm *.txt\n'

#Build up reformatting command (IRIS Movies have different sizes and naming)
if len(movielist) != 0:
    #rename so files from same time are listed together regardless of name
    for mp4 in movielist:
        if mp4[0:2] == 'l2':
            movie_name = mp4[3:]
            os.rename(mp4,movie_name)
        if mp4[0:2] == 'PS':
            movie_name = mp4[10:]
            os.rename(mp4,movie_name)
        if mp4[0:4] == 'iris':
            movie_name = mp4[-19:]
            os.rename(mp4,movie_name)
    #get list of new names and reformat
    filelist = os.listdir(movie_dir)
    movielist = [m for m in filelist if ".mp4" in m]      
    for mp4 in movielist:
        reformatted_list = os.listdir(movie_dir+'/Reformatted')
        #only create reformatted video if not already in reformat directory
        if mp4 not in reformatted_list:
            reformat_com = reformat_com + '\n'+'ffmpeg -i '+mp4+' -vf "scale=1600:900:force_original_aspect_ratio=decrease,pad=1600:900:(ow-iw)/2:(oh-ih)/2" Reformatted/'+mp4

if len(movielist) == 0:
    print('No IRIS movies found. Please add movies to the IRIS Movie directory and try again.')
    remformat_com =''
    merge_com = 'cd Reformatted\n'
    
#####################################################
#    Write and Exucute all the built commands       #
#####################################################
os.chdir(cwd)
full_command = '#!/bin/tcsh\n'+'cd IRIS_Movies\n'+reformat_com+merge_com+move_com+'\n'+'cd ../../'+'\n'+'#end'
 
#Write all instructions to .csh file that the user can exucute 
com = open('IRIS_Movie_Command.csh','w')
com.write(full_command)
com.close()

#change file to executable
mod = subprocess.call(['/bin/csh','-c','chmod a+x IRIS_Movie_Command.csh'])

#run ffmpeg
run = subprocess.call(['/bin/csh','-c','./IRIS_Movie_Command.csh'])
   