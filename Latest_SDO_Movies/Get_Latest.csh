#!/bin/tcsh
rm *.mp4
wget https://sdo.gsfc.nasa.gov/assets/img/latest/latest_1024_0094.mp4
wget https://sdo.gsfc.nasa.gov/assets/img/latest/latest_1024_0304.mp4
wget https://sdo.gsfc.nasa.gov/assets/img/latest/latest_1024_0193.mp4
wget https://sdo.gsfc.nasa.gov/assets/img/latest/latest_1024_0171.mp4
wget https://sdo.gsfc.nasa.gov/assets/img/latest/latest_1024_1600.mp4
wget https://sdo.gsfc.nasa.gov/assets/img/latest/latest_1024_fade.mp4

ffmpeg -nostdin -i latest_1024_fade.mp4 -i latest_1024_0193.mp4 -i latest_1024_0304.mp4 -i latest_1024_0094.mp4 -i latest_1024_0171.mp4 -i latest_1024_1600.mp4 -filter_complex "color=s=3200x1800:c=black [base];[0:v] setpts=PTS-STARTPTS, scale=1200x1200 [a];[1:v] setpts=PTS-STARTPTS, scale=600x600 [b];[2:v] setpts=PTS-STARTPTS, scale=600x600 [c];[3:v] setpts=PTS-STARTPTS, scale=600x600 [d];[4:v] setpts=PTS-STARTPTS, scale=600x600 [e];[5:v] setpts=PTS-STARTPTS, scale=600x600 [f];[base][a] overlay=shortest=1:x=650[tmp1];[tmp1][b] overlay=shortest=1:x=2368[tmp2];[tmp2][c] overlay=shortest=1:x=2368:y=600[tmp3];[tmp3][d] overlay=shortest=1:x=233:y=1200[tmp4];[tmp4][e] overlay=shortest=1:x=1300:y=1200[tmp5];[tmp5][f] overlay=shortest=1:x=2368:y=1200" -y TEMP_Weather_Video.mp4
echo file TEMP_Weather_Video.mp4 >> TEMP.txt
#echo file TEMP_Weather_Video.mp4 >> TEMP.txt
#echo file TEMP_Weather_Video.mp4 >> TEMP.txt

ffmpeg -nostdin -f concat -safe 0 -i TEMP.txt -filter:v "setpts=1.5*PTS"  Latest_Weather_Video.mp4
rm *TEMP*
cp Latest_Weather_Video.mp4 ../VIDEO_WALL_DISPLAY/Latest_Weather_Video.mp4
#end