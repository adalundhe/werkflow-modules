from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .code_pipeline_target_filter import CodePipelineTargetFilter


class CodePipelineListDeployActionExecutionTargetsRequest(BaseModel):
    actionExecutionId: StrictStr
    pipelineName: StrictStr | None = None
    filters: list[CodePipelineTargetFilter] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
