from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_pipeline_pipeline_summary import CodePipelinePipelineSummary


class CodePipelineListPipelinesResponse(BaseModel):
    pipelines: list[CodePipelinePipelineSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
