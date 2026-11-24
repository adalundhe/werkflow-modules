from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .code_pipeline_pipeline_declaration import CodePipelinePipelineDeclaration
from .code_pipeline_tag import CodePipelineTag


class CodePipelineCreatePipelineResponse(BaseModel):
    pipeline: CodePipelinePipelineDeclaration | None = None
    tags: list[CodePipelineTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
