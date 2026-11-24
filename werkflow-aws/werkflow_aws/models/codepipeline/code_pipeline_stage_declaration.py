from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_pipeline_action_declaration import CodePipelineActionDeclaration
from .code_pipeline_before_entry_conditions import CodePipelineBeforeEntryConditions
from .code_pipeline_blocker_declaration import CodePipelineBlockerDeclaration
from .code_pipeline_failure_conditions import CodePipelineFailureConditions
from .code_pipeline_success_conditions import CodePipelineSuccessConditions


class CodePipelineStageDeclaration(BaseModel):
    name: StrictStr | None = None
    blockers: list[CodePipelineBlockerDeclaration] | None = None
    actions: list[CodePipelineActionDeclaration] | None = None
    onFailure: CodePipelineFailureConditions | None = None
    onSuccess: CodePipelineSuccessConditions | None = None
    beforeEntry: CodePipelineBeforeEntryConditions | None = None
