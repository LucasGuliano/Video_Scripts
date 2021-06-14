#!/bin/tcsh
cd STEREO
rm *
set ddate=20210507
rm *.txt
find *.mpg >> temp.txt
foreach v (`cat temp.txt`)
echo file $v >> mag_file_list.txt
end
ffmpeg -nostdin -f concat -safe 0 -i mag_file_list.txt STEREO_Far_Side.mp4
ffmpeg -nostdin -i STEREO_Far_Side.mp4 -filter:v "setpts=0.5*PTS" STEREO_Far_Side.mp4_${ddate}.mp4
rm *.txt

cd ..
rm Nine_Quadrant_Movies/*
cd 0094
wget https://sdo.gsfc.nasa.gov/assets/img/dailymov/2021/05/07/20210507_1024_0094.mp4
rm *.txt
find *.mp4 >> temp.txt
foreach v (`cat temp.txt`)
echo file $v >> file_list.txt
end
ffmpeg -nostdin -f concat -safe 0 -i file_list.txt ../Nine_Quadrant_Movies/0094.mp4
rm *.txt
cd ../

cd 0131
wget https://sdo.gsfc.nasa.gov/assets/img/dailymov/2021/05/07/20210507_1024_0131.mp4
rm *.txt
find *.mp4 >> temp.txt
foreach v (`cat temp.txt`)
echo file $v >> file_list.txt
end
ffmpeg -nostdin -f concat -safe 0 -i file_list.txt ../Nine_Quadrant_Movies/0131.mp4
rm *.txt
cd ../

cd 0171
wget https://sdo.gsfc.nasa.gov/assets/img/dailymov/2021/05/07/20210507_1024_0171.mp4
rm *.txt
find *.mp4 >> temp.txt
foreach v (`cat temp.txt`)
echo file $v >> file_list.txt
end
ffmpeg -nostdin -f concat -safe 0 -i file_list.txt ../Nine_Quadrant_Movies/0171.mp4
rm *.txt
cd ../

cd 0211
wget https://sdo.gsfc.nasa.gov/assets/img/dailymov/2021/05/07/20210507_1024_0211.mp4
rm *.txt
find *.mp4 >> temp.txt
foreach v (`cat temp.txt`)
echo file $v >> file_list.txt
end
ffmpeg -nostdin -f concat -safe 0 -i file_list.txt ../Nine_Quadrant_Movies/0211.mp4
rm *.txt
cd ../

cd 0193
wget https://sdo.gsfc.nasa.gov/assets/img/dailymov/2021/05/07/20210507_1024_0193.mp4
rm *.txt
find *.mp4 >> temp.txt
foreach v (`cat temp.txt`)
echo file $v >> file_list.txt
end
ffmpeg -nostdin -f concat -safe 0 -i file_list.txt ../Nine_Quadrant_Movies/0193.mp4
rm *.txt
cd ../

cd 0304
wget https://sdo.gsfc.nasa.gov/assets/img/dailymov/2021/05/07/20210507_1024_0304.mp4
rm *.txt
find *.mp4 >> temp.txt
foreach v (`cat temp.txt`)
echo file $v >> file_list.txt
end
ffmpeg -nostdin -f concat -safe 0 -i file_list.txt ../Nine_Quadrant_Movies/0304.mp4
rm *.txt
cd ../

cd 0335
wget https://sdo.gsfc.nasa.gov/assets/img/dailymov/2021/05/07/20210507_1024_0335.mp4
rm *.txt
find *.mp4 >> temp.txt
foreach v (`cat temp.txt`)
echo file $v >> file_list.txt
end
ffmpeg -nostdin -f concat -safe 0 -i file_list.txt ../Nine_Quadrant_Movies/0335.mp4
rm *.txt
cd ../

cd 1600
wget https://sdo.gsfc.nasa.gov/assets/img/dailymov/2021/05/07/20210507_1024_1600.mp4
rm *.txt
find *.mp4 >> temp.txt
foreach v (`cat temp.txt`)
echo file $v >> file_list.txt
end
ffmpeg -nostdin -f concat -safe 0 -i file_list.txt ../Nine_Quadrant_Movies/1600.mp4
rm *.txt
cd ../

cd 1700
wget https://sdo.gsfc.nasa.gov/assets/img/dailymov/2021/05/07/20210507_1024_1700.mp4
rm *.txt
find *.mp4 >> temp.txt
foreach v (`cat temp.txt`)
echo file $v >> file_list.txt
end
ffmpeg -nostdin -f concat -safe 0 -i file_list.txt ../Nine_Quadrant_Movies/1700.mp4
rm *.txt
cd ../


cd Nine_Quadrant_Movies
ffmpeg -i 0094.mp4 -i 0131.mp4 -i 0171.mp4 -i 0211.mp4 -i 0193.mp4 -i 0304.mp4 -i 0335.mp4 -i 1600.mp4 -i 1700.mp4 -filter_complex "color=s=3200x1800:c=black [base];[0:v] setpts=PTS-STARTPTS, scale=600x600 [a];[1:v] setpts=PTS-STARTPTS, scale=600x600 [b];[2:v] setpts=PTS-STARTPTS, scale=600x600 [c];[3:v] setpts=PTS-STARTPTS, scale=600x600 [d];[4:v] setpts=PTS-STARTPTS, scale=600x600 [e];[5:v] setpts=PTS-STARTPTS, scale=600x600 [f];[6:v] setpts=PTS-STARTPTS, scale=550x550 [g];[7:v] setpts=PTS-STARTPTS, scale=550x550 [h];[8:v] setpts=PTS-STARTPTS, scale=550x550 [i];[base][a] overlay=shortest=1:x=233[tmp1];[tmp1][b] overlay=shortest=1:x=1300[tmp2];[tmp2][c] overlay=shortest=1:x=2368[tmp3];[tmp3][d] overlay=shortest=1:x=233:y=600[tmp4];[tmp4][e] overlay=shortest=1:x=1300:y=600[tmp5];[tmp5][f] overlay=shortest=1:x=2368:y=600[tmp6];[tmp6][g] overlay=shortest=1:x=233:y=1250[tmp7];[tmp7][h] overlay=shortest=1:x=1300:y=1250[tmp8];[tmp8][i] overlay=shortest=1:x=2368:y=1250" -y Nine_Quadrant_Video.mp4
cp Nine_Quadrant_Video.mp4 ../../VIDEO_WALL_DISPLAY/Nine_Quadrant_Video.mp4
#end