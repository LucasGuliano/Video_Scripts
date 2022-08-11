#!/bin/tcsh
tar -xf images.zip

ffmpeg -framerate 30 -pattern_type glob -i '*.jpg' -c:v libx264 -r 30 -pix_fmt yuv420p CME1.mp4

ffmpeg -i CME1.mp4 -vf "scale=3200:1800:force_original_aspect_ratio=decrease,pad=3200:1800:(ow-iw)/2:(oh-ih)/2" CME.mp4


mv CME.mp4 ../VIDEO_WALL_DISPLAY
rm *.mp4
rm *.jpg
