from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .code_pipeline_rule_type import CodePipelineRuleType


class CodePipelineListRuleTypesResponse(BaseModel):
    ruleTypes: list[CodePipelineRuleType] | None = None
    ResponseMetadata: dict[str, Any] | None = None
