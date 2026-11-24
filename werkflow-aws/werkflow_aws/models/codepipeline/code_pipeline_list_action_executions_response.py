from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_pipeline_action_execution_detail import CodePipelineActionExecutionDetail


class CodePipelineListActionExecutionsResponse(BaseModel):
    actionExecutionDetails: list[CodePipelineActionExecutionDetail] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
