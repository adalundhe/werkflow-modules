from __future__ import annotations
from pydantic import BaseModel
from .ssm_automation_execution_inputs import SSMAutomationExecutionInputs


class SSMExecutionInputs(BaseModel):
    Automation: SSMAutomationExecutionInputs | None = None
