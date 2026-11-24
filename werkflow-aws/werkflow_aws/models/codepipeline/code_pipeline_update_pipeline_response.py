from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .code_pipeline_pipeline_declaration import CodePipelinePipelineDeclaration


class CodePipelineUpdatePipelineResponse(BaseModel):
    pipeline: CodePipelinePipelineDeclaration | None = None
    ResponseMetadata: dict[str, Any] | None = None
