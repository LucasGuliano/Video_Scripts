#!/bin/tcsh

cd HMIBC
wget --no-check-certificate https://sdo.gsfc.nasa.gov/assets/img/dailymov/2022/06/18/20220618_1024_HMIBC.mp4
wget --no-check-certificate https://sdo.gsfc.nasa.gov/assets/img/dailymov/2022/06/19/20220619_1024_HMIBC.mp4
wget --no-check-certificate https://sdo.gsfc.nasa.gov/assets/img/dailymov/2022/06/20/20220620_1024_HMIBC.mp4
wget --no-check-certificate https://sdo.gsfc.nasa.gov/assets/img/dailymov/2022/06/21/20220621_1024_HMIBC.mp4
wget --no-check-certificate https://sdo.gsfc.nasa.gov/assets/img/dailymov/2022/06/22/20220622_1024_HMIBC.mp4
wget --no-check-certificate https://sdo.gsfc.nasa.gov/assets/img/dailymov/2022/06/23/20220623_1024_HMIBC.mp4
wget --no-check-certificate https://sdo.gsfc.nasa.gov/assets/img/dailymov/2022/06/24/20220624_1024_HMIBC.mp4
wget --no-check-certificate https://sdo.gsfc.nasa.gov/assets/img/dailymov/2022/06/25/20220625_1024_HMIBC.mp4
wget --no-check-certificate https://sdo.gsfc.nasa.gov/assets/img/dailymov/2022/06/26/20220626_1024_HMIBC.mp4
wget --no-check-certificate https://sdo.gsfc.nasa.gov/assets/img/dailymov/2022/06/27/20220627_1024_HMIBC.mp4
wget --no-check-certificate https://sdo.gsfc.nasa.gov/assets/img/dailymov/2022/06/28/20220628_1024_HMIBC.mp4
wget --no-check-certificate https://sdo.gsfc.nasa.gov/assets/img/dailymov/2022/06/29/20220629_1024_HMIBC.mp4
wget --no-check-certificate https://sdo.gsfc.nasa.gov/assets/img/dailymov/2022/06/30/20220630_1024_HMIBC.mp4
wget --no-check-certificate https://sdo.gsfc.nasa.gov/assets/img/dailymov/2022/07/01/20220701_1024_HMIBC.mp4
wget --no-check-certificate https://sdo.gsfc.nasa.gov/assets/img/dailymov/2022/07/02/20220702_1024_HMIBC.mp4
wget --no-check-certificate https://sdo.gsfc.nasa.gov/assets/img/dailymov/2022/07/03/20220703_1024_HMIBC.mp4
wget --no-check-certificate https://sdo.gsfc.nasa.gov/assets/img/dailymov/2022/07/04/20220704_1024_HMIBC.mp4
wget --no-check-certificate https://sdo.gsfc.nasa.gov/assets/img/dailymov/2022/07/05/20220705_1024_HMIBC.mp4
wget --no-check-certificate https://sdo.gsfc.nasa.gov/assets/img/dailymov/2022/07/06/20220706_1024_HMIBC.mp4
wget --no-check-certificate https://sdo.gsfc.nasa.gov/assets/img/dailymov/2022/07/07/20220707_1024_HMIBC.mp4
wget --no-check-certificate https://sdo.gsfc.nasa.gov/assets/img/dailymov/2022/07/08/20220708_1024_HMIBC.mp4
wget --no-check-certificate https://sdo.gsfc.nasa.gov/assets/img/dailymov/2022/07/09/20220709_1024_HMIBC.mp4
wget --no-check-certificate https://sdo.gsfc.nasa.gov/assets/img/dailymov/2022/07/10/20220710_1024_HMIBC.mp4
wget --no-check-certificate https://sdo.gsfc.nasa.gov/assets/img/dailymov/2022/07/11/20220711_1024_HMIBC.mp4
wget --no-check-certificate https://sdo.gsfc.nasa.gov/assets/img/dailymov/2022/07/12/20220712_1024_HMIBC.mp4
wget --no-check-certificate https://sdo.gsfc.nasa.gov/assets/img/dailymov/2022/07/13/20220713_1024_HMIBC.mp4
wget --no-check-certificate https://sdo.gsfc.nasa.gov/assets/img/dailymov/2022/07/14/20220714_1024_HMIBC.mp4
wget --no-check-certificate https://sdo.gsfc.nasa.gov/assets/img/dailymov/2022/07/15/20220715_1024_HMIBC.mp4
wget --no-check-certificate https://sdo.gsfc.nasa.gov/assets/img/dailymov/2022/07/16/20220716_1024_HMIBC.mp4
wget --no-check-certificate https://sdo.gsfc.nasa.gov/assets/img/dailymov/2022/07/17/20220717_1024_HMIBC.mp4
rm *.txt
find *.mp4 >> temp.txt
foreach v (`cat temp.txt`)
echo file $v >> file_list.txt
end
ffmpeg -nostdin -f concat -safe 0 -i file_list.txt HMIBC.mp4
rm *.txt

ffmpeg -i HMIBC.mp4 -vf "scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2" Magnetic_Month.mp4
mv Magnetic_Month.mp4 ../../VIDEO_WALL_DISPLAY
cd ../
rm -R HMIBC
#end