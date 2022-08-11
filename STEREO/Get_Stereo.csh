#!/bin/tcsh

set full_date = `date -v -1d '+%Y%m%d'`
set year = `date -v -1d '+%Y'`
set month = `date -v -1d '+%m'`
set day = `date -v -1d '+%d'`

wget --no-check-certificate https://stereo-ssc.nascom.nasa.gov/browse/$year/$month/$day/ahead_${full_date}_euvi_195_512.mpg

ffmpeg -i ahead*.mpg -filter:v "setpts=5.00*PTS" stereo.mp4

ffmpeg -i stereo.mp4 -vf "scale=3200:1800:force_original_aspect_ratio=decrease,pad=3200:1800:(ow-iw)/2:(oh-ih)/2" stereo_ahead.mp4

rm stereo.mp4
rm ahead*.mpg
mv stereo_ahead.mp4 ../VIDEO_WALL_DISPLAY

#end
