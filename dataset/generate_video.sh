filename="theatre_timelapse.mp4"

cd theatre_dataset_images

for i in *.jpg; 
 do   
  echo "file '$i'" >> files.txt;
  replaced=${i// /_}
  substr=${replaced:0:16} 
  echo "file_packet_metadata url=${substr}" >> files.txt; 
 done

ffmpeg -r 25 -f concat -safe 0 -i files.txt -vf "drawtext=text='%{metadata\:url}': fontcolor=0xffffff: fontsize=24: x=w-tw-30:y=h-th-10" -s:v 1440x1152  -c:v libx264 $filename

rm files.txt
mv $filename ./..
