from typing import List

from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(title="VideoSwift Backend", version="0.5.0")


class SummarizeRequest(BaseModel):
    video_url: str = Field(..., min_length=1, description="Video URL from the frontend")


class Chapter(BaseModel):
    title: str
    start_time: str
    summary: str


class SummarizeResponse(BaseModel):
    summary: str
    key_points: List[str]
    chapters: List[Chapter]
    action_items: List[str]
    use_cases: List[str]


@app.post("/api/summarize", response_model=SummarizeResponse)
def summarize_video(payload: SummarizeRequest) -> SummarizeResponse:
    source_url = payload.video_url

    return SummarizeResponse(
        summary=f"这是一个针对视频链接 {source_url} 的模拟总结结果，后续将替换为真实 AI 分析输出。",
        key_points=[
            "视频内容围绕核心主题展开，重点信息清晰。",
            "讲解过程包含背景说明、重点分析和行动建议。",
            "当前接口返回的是固定结构的模拟数据。",
        ],
        chapters=[
            Chapter(
                title="开场与主题介绍",
                start_time="00:00",
                summary="介绍视频主题、背景和目标。",
            ),
            Chapter(
                title="核心内容展开",
                start_time="01:20",
                summary="围绕主要观点进行拆解和说明。",
            ),
            Chapter(
                title="总结与行动建议",
                start_time="05:40",
                summary="整理结论并给出可执行建议。",
            ),
        ],
        action_items=[
            "整理视频中的关键观点，形成可复用笔记。",
            "根据章节摘要回顾重点内容。",
            "后续接入真实字幕获取与 AI 总结流程。",
        ],
        use_cases=[
            "快速了解长视频的核心内容。",
            "将课程、会议或访谈转成结构化笔记。",
            "帮助用户快速提炼可执行行动清单。",
        ],
    )
