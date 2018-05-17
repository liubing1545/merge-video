# -*- coding: utf-8 -*-

from moviepy.editor import *
import os

L = []

# 遍历 video 文件夹
for root, dirs, files in os.walk("./video"):
    # 按文件名排序
    files.sort()
    for file in files:
        # 如果后缀名为 .mp4
        if os.path.splitext(file)[1] == '.mp4':
            filePath = os.path.join(root, file)
            video = VideoFileClip(filePath)
            L.append(video)

# 拼接视频
final_clip = concatenate_videoclips(L)

# 生成目标视频文件
final_clip.to_videofile("./target.mp4", fps=24, remove_temp=False)
