from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_pipeline_action_context import CodePipelineActionContext
from .code_pipeline_stage_context import CodePipelineStageContext


class CodePipelinePipelineContext(BaseModel):
    pipelineName: StrictStr | None = None
    stage: CodePipelineStageContext | None = None
    action: CodePipelineActionContext | None = None
    pipelineArn: StrictStr | None = None
    pipelineExecutionId: StrictStr | None = None
