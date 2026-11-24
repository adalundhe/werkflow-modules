from __future__ import annotations
from pydantic import BaseModel
from .code_pipeline_rule_execution_result import CodePipelineRuleExecutionResult


class CodePipelineRuleExecutionOutput(BaseModel):
    executionResult: CodePipelineRuleExecutionResult | None = None
