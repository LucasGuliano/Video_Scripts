#!/bin/tcsh

cd 0193
wget https://sdo.gsfc.nasa.gov/assets/img/dailymov/2021/05/25/20210525_1024_0193.mp4
wget https://sdo.gsfc.nasa.gov/assets/img/dailymov/2021/05/26/20210526_1024_0193.mp4
wget https://sdo.gsfc.nasa.gov/assets/img/dailymov/2021/05/27/20210527_1024_0193.mp4
wget https://sdo.gsfc.nasa.gov/assets/img/dailymov/2021/05/28/20210528_1024_0193.mp4
wget https://sdo.gsfc.nasa.gov/assets/img/dailymov/2021/05/29/20210529_1024_0193.mp4
wget https://sdo.gsfc.nasa.gov/assets/img/dailymov/2021/05/30/20210530_1024_0193.mp4
wget https://sdo.gsfc.nasa.gov/assets/img/dailymov/2021/05/31/20210531_1024_0193.mp4
rm *.txt
find *.mp4 >> temp.txt
foreach v (`cat temp.txt`)
echo file $v >> file_list.txt
end
ffmpeg -nostdin -f concat -safe 0 -i file_list.txt 0193_20210525_to_20210601.mp4
rm *.txt

mv 0193_20210525_to_20210601.mp4 ../Single_Wave_Movies
cd ../
rm -R 0193
#end