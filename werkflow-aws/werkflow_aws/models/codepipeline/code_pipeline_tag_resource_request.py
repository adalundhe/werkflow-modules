from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_pipeline_tag import CodePipelineTag


class CodePipelineTagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tags: list[CodePipelineTag]
