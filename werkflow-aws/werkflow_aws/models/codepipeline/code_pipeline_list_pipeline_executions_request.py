from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .code_pipeline_pipeline_execution_filter import CodePipelinePipelineExecutionFilter


class CodePipelineListPipelineExecutionsRequest(BaseModel):
    pipelineName: StrictStr
    maxResults: StrictInt | None = None
    filter: CodePipelinePipelineExecutionFilter | None = None
    nextToken: StrictStr | None = None
