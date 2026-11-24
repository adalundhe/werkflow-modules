from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_pipeline_pipeline_execution_summary import CodePipelinePipelineExecutionSummary


class CodePipelineListPipelineExecutionsResponse(BaseModel):
    pipelineExecutionSummaries: list[CodePipelinePipelineExecutionSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
