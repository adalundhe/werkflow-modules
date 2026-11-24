from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .code_pipeline_deploy_target_event_context import CodePipelineDeployTargetEventContext


class CodePipelineDeployTargetEvent(BaseModel):
    name: StrictStr | None = None
    status: StrictStr | None = None
    startTime: datetime.datetime | StrictStr | None = None
    endTime: datetime.datetime | StrictStr | None = None
    context: CodePipelineDeployTargetEventContext | None = None
