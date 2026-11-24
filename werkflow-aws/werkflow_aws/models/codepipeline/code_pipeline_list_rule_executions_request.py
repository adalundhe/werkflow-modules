from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .code_pipeline_rule_execution_filter import CodePipelineRuleExecutionFilter


class CodePipelineListRuleExecutionsRequest(BaseModel):
    pipelineName: StrictStr
    filter: CodePipelineRuleExecutionFilter | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
