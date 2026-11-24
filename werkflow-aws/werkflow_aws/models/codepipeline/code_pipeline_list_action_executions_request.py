from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .code_pipeline_action_execution_filter import CodePipelineActionExecutionFilter


class CodePipelineListActionExecutionsRequest(BaseModel):
    pipelineName: StrictStr
    filter: CodePipelineActionExecutionFilter | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
