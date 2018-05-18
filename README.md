# merge-video
合并MP4视频    
新建video文件夹将需要合并的视频文件放入其中

### 安装依赖
```shell
pip install -r requirements.txt
```
### 执行
```python
python ffmpeg.py
python merge.py
```
### ffmpeg直接转换拼接
```shell
ffmpeg.exe -i video\1.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts input1.ts
ffmpeg.exe -i video\2.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts input2.ts
ffmpeg.exe -i video\3.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts input3.ts
ffmpeg.exe -i video\4.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts input4.ts
ffmpeg.exe -i video\5.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts input5.ts
ffmpeg -i "concat:input1.ts|input2.ts|input3.ts|input4.ts|input5.ts" -c copy -bsf:a aac_adtstoasc -movflags +faststart output.mp4
```

