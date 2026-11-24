from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .code_pipeline_pipeline_declaration import CodePipelinePipelineDeclaration
from .code_pipeline_pipeline_metadata import CodePipelinePipelineMetadata


class CodePipelineGetPipelineResponse(BaseModel):
    pipeline: CodePipelinePipelineDeclaration | None = None
    metadata: CodePipelinePipelineMetadata | None = None
    ResponseMetadata: dict[str, Any] | None = None
