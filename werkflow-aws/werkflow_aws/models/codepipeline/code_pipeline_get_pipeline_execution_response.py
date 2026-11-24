from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .code_pipeline_pipeline_execution import CodePipelinePipelineExecution


class CodePipelineGetPipelineExecutionResponse(BaseModel):
    pipelineExecution: CodePipelinePipelineExecution | None = None
    ResponseMetadata: dict[str, Any] | None = None
