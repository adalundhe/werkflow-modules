from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_pipeline_action_revision import CodePipelineActionRevision


class CodePipelinePutActionRevisionRequest(BaseModel):
    pipelineName: StrictStr
    stageName: StrictStr
    actionName: StrictStr
    actionRevision: CodePipelineActionRevision
