# ffmpeg_mp42h264
ffmpeg.exe를 사용해서 영상 파일들을 H264 코덱의 mp4 파일로 변경

## 사용법1 (mp4파일을 코덱만 H264로 변경)
1. ffmpeg 다운로드 (https://ffmpeg.org/download.html)
2. 빈 폴더에 ffmpeg.exe, ffmpeg_convert.py, convert.py 위치
3. 해당 폴더에 H264 코덱으로 변경하고자 하는 mp4 파일 넣기
4. convert.bat 실행
5. 기존파일명_h264.mp4 파일 생성


## 사용법2 (원하는 확장자의 파일을 H264 코덱의 mp4 파일로 변경)
1. ffmpeg 다운로드 (https://ffmpeg.org/download.html)
2. 빈 폴더에 ffmpeg.exe, ffmpeg_convert.py 위치
3. 해당 폴더에 H264 코덱으로 변경하고자 하는 mp4 파일 넣기
4. cmd에서 `python ffmpeg_convert.py {|mp4|MOV|...}` 실행
