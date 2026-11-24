from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_pipeline_latest_in_pipeline_execution_filter import CodePipelineLatestInPipelineExecutionFilter


class CodePipelineActionExecutionFilter(BaseModel):
    pipelineExecutionId: StrictStr | None = None
    latestInPipelineExecution: CodePipelineLatestInPipelineExecutionFilter | None = None
