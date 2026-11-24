from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .emr_step_config import EMRStepConfig


class EMRAddJobFlowStepsRequest(BaseModel):
    JobFlowId: StrictStr
    Steps: list[EMRStepConfig]
    ExecutionRoleArn: StrictStr | None = None
