from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_pipeline_rule_execution_detail import CodePipelineRuleExecutionDetail


class CodePipelineListRuleExecutionsResponse(BaseModel):
    ruleExecutionDetails: list[CodePipelineRuleExecutionDetail] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
