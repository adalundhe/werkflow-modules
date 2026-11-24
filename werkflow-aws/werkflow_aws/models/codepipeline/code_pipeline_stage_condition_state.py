from __future__ import annotations
from pydantic import BaseModel
from .code_pipeline_condition_state import CodePipelineConditionState
from .code_pipeline_stage_conditions_execution import CodePipelineStageConditionsExecution


class CodePipelineStageConditionState(BaseModel):
    latestExecution: CodePipelineStageConditionsExecution | None = None
    conditionStates: list[CodePipelineConditionState] | None = None
