from __future__ import annotations
from pydantic import BaseModel
from .code_pipeline_pipeline_declaration import CodePipelinePipelineDeclaration
from .code_pipeline_tag import CodePipelineTag


class CodePipelineCreatePipelineRequest(BaseModel):
    pipeline: CodePipelinePipelineDeclaration
    tags: list[CodePipelineTag] | None = None
