# -*- coding: utf-8 -*-

import imageio
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# 下载 ffmpeg 组件
imageio.plugins.ffmpeg.download()
