from __future__ import annotations
from pydantic import BaseModel
from .code_pipeline_pipeline_declaration import CodePipelinePipelineDeclaration


class CodePipelineUpdatePipelineRequest(BaseModel):
    pipeline: CodePipelinePipelineDeclaration
