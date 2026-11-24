from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_pipeline_action_execution import CodePipelineActionExecution
from .code_pipeline_action_revision import CodePipelineActionRevision


class CodePipelineActionState(BaseModel):
    actionName: StrictStr | None = None
    currentRevision: CodePipelineActionRevision | None = None
    latestExecution: CodePipelineActionExecution | None = None
    entityUrl: StrictStr | None = None
    revisionUrl: StrictStr | None = None
