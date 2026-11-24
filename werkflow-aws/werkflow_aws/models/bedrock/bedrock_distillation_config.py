from __future__ import annotations
from pydantic import BaseModel
from .bedrock_teacher_model_config import BedrockTeacherModelConfig


class BedrockDistillationConfig(BaseModel):
    teacherModelConfig: BedrockTeacherModelConfig | None = None
