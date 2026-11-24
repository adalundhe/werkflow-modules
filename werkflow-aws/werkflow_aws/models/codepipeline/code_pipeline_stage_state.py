from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_pipeline_action_state import CodePipelineActionState
from .code_pipeline_retry_stage_metadata import CodePipelineRetryStageMetadata
from .code_pipeline_stage_condition_state import CodePipelineStageConditionState
from .code_pipeline_stage_execution import CodePipelineStageExecution
from .code_pipeline_transition_state import CodePipelineTransitionState


class CodePipelineStageState(BaseModel):
    stageName: StrictStr | None = None
    inboundExecution: CodePipelineStageExecution | None = None
    inboundExecutions: list[CodePipelineStageExecution] | None = None
    inboundTransitionState: CodePipelineTransitionState | None = None
    actionStates: list[CodePipelineActionState] | None = None
    latestExecution: CodePipelineStageExecution | None = None
    beforeEntryConditionState: CodePipelineStageConditionState | None = None
    onSuccessConditionState: CodePipelineStageConditionState | None = None
    onFailureConditionState: CodePipelineStageConditionState | None = None
    retryStageMetadata: CodePipelineRetryStageMetadata | None = None
