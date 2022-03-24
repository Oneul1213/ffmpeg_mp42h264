import os, sys

ext = ""
if len(sys.argv) == 2:
    ext = sys.argv[1]
else:
    ext = "mp4"

video_files = os.popen(f'dir/b *.{ext}').read().split()
video_files = [path[:-4] for path in video_files]
# print(video_files)
for fileName in video_files:
    print(f"##### current file : {fileName}.{ext} #####" )
    print("##### convert to h264 #####")
    os.system(f'ffmpeg -i "{fileName}.{ext}" -c:v libx264 -c:a copy -preset ultrafast -crf 18 "{fileName}_h264.mp4"')
