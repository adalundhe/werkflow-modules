from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .code_pipeline_deploy_target_event import CodePipelineDeployTargetEvent


class CodePipelineDeployActionExecutionTarget(BaseModel):
    targetId: StrictStr | None = None
    targetType: StrictStr | None = None
    status: StrictStr | None = None
    startTime: datetime.datetime | StrictStr | None = None
    endTime: datetime.datetime | StrictStr | None = None
    events: list[CodePipelineDeployTargetEvent] | None = None
