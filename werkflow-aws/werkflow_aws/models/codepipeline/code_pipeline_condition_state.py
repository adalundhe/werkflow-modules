from __future__ import annotations
from pydantic import BaseModel
from .code_pipeline_condition_execution import CodePipelineConditionExecution
from .code_pipeline_rule_state import CodePipelineRuleState


class CodePipelineConditionState(BaseModel):
    latestExecution: CodePipelineConditionExecution | None = None
    ruleStates: list[CodePipelineRuleState] | None = None
