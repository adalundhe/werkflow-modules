from __future__ import annotations
from pydantic import BaseModel
from .code_pipeline_condition import CodePipelineCondition


class CodePipelineSuccessConditions(BaseModel):
    conditions: list[CodePipelineCondition] | None = None
