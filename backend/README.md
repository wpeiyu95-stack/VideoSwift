# Backend

VideoSwift 的后端会在未来负责处理视频总结的核心业务流程。

## 未来职责

- 接收前端提交的视频链接
- 获取视频字幕
- 调用 AI API 生成总结结果
- 返回结构化总结数据给前端

## 当前状态

当前后端仍处于规划阶段，不接入真实 API，也不包含真实密钥配置。

## 本地运行

1. 进入 backend 目录。
2. 安装依赖：

	```bash
	pip install -r requirements.txt
	```

3. 启动服务：

	```bash
	uvicorn app:app --reload --host 127.0.0.1 --port 8000
	```

## 接口说明

### POST /api/summarize

请求体示例：

```json
{
  "video_url": "https://example.com/video"
}
```

返回内容为模拟总结数据，包含 `summary`、`key_points`、`chapters`、`action_items` 和 `use_cases`。

