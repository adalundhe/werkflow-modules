from __future__ import annotations
from pydantic import BaseModel
from .emr_step_config import EMRStepConfig
from .emr_step_execution_status_detail import EMRStepExecutionStatusDetail


class EMRStepDetail(BaseModel):
    StepConfig: EMRStepConfig | None = None
    ExecutionStatusDetail: EMRStepExecutionStatusDetail | None = None
