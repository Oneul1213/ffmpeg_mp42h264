import os

mp4_files = os.popen('dir/b *.mp4').read().split()
mp4_files = [path[:-4] for path in mp4_files]
# print(mp4_files)
for fileName in mp4_files:
    print(f'##### current file : {fileName}.mp4 #####' )
    print("##### convert to h264 #####")
    os.system(f'ffmpeg -i "{fileName}.mp4" -c:v libx264 -c:a copy -preset ultrafast -crf 18 "{fileName}_h264.mp4"')
