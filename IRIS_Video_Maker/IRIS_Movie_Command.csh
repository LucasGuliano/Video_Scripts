#!/bin/tcsh
cd IRIS_Movies

ffmpeg -i 20210521_165943_3622606133_SJI_1330_t000_fits_20210521_165943_m.mp4 -vf "scale=1600:900:force_original_aspect_ratio=decrease,pad=1600:900:(ow-iw)/2:(oh-ih)/2" Reformatted/20210521_165943_3622606133_SJI_1330_t000_fits_20210521_165943_m.mp4
ffmpeg -i 20210522_121113_3660259533_SJI_1330_t000_fits_20210522_121113_m.mp4 -vf "scale=1600:900:force_original_aspect_ratio=decrease,pad=1600:900:(ow-iw)/2:(oh-ih)/2" Reformatted/20210522_121113_3660259533_SJI_1330_t000_fits_20210522_121113_m.mp4
ffmpeg -i 20210522_170743_3622606133_SJI_1330_t000_fits_20210522_170743_m.mp4 -vf "scale=1600:900:force_original_aspect_ratio=decrease,pad=1600:900:(ow-iw)/2:(oh-ih)/2" Reformatted/20210522_170743_3622606133_SJI_1330_t000_fits_20210522_170743_m.mp4
ffmpeg -i 20210522_231021_3660259533_SJI_1330_t000_fits_20210522_231021_m.mp4 -vf "scale=1600:900:force_original_aspect_ratio=decrease,pad=1600:900:(ow-iw)/2:(oh-ih)/2" Reformatted/20210522_231021_3660259533_SJI_1330_t000_fits_20210522_231021_m.mp4
ffmpeg -i 20210523_165943_3622606133_SJI_1330_t000_fits_20210523_165943_m.mp4 -vf "scale=1600:900:force_original_aspect_ratio=decrease,pad=1600:900:(ow-iw)/2:(oh-ih)/2" Reformatted/20210523_165943_3622606133_SJI_1330_t000_fits_20210523_165943_m.mp4
cd Reformatted
find *.mp4 >> temp.txt
foreach v ( `cat temp.txt` )
echo file $v >> IRIS_file_list.txt
end
ffmpeg -nostdin -f concat -safe 0 -i IRIS_file_list.txt -y IRIS_Highlight_Video.mp4

cp IRIS_Highlight_Video.mp4 ../../../VIDEO_WALL_DISPLAY
mv IRIS_Highlight_Video.mp4 ../../
rm *.txt

cd ../../
#end