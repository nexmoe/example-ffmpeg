
# 视频转换 API

这是一个简单的视频转换 API 服务,可以将上传的视频转换为 MP4 格式。

## 功能

- 提供 Web 界面上传视频文件
- 使用 FFmpeg 将视频转换为 MP4 格式  
- 支持下载转换后的 MP4 视频

## 技术栈

- 后端: FastAPI
- 前端: Vue.js
- 视频处理: FFmpeg

## Docker 构建

提供了 Dockerfile,可以使用以下命令构建和运行:

```sh
docker build -t example-ffmpeg .
docker run -p 8000:8000 example-ffmpeg
``
