from __future__ import annotations
from pydantic import BaseModel
from .ssm_automation_execution_preview import SSMAutomationExecutionPreview


class SSMExecutionPreview(BaseModel):
    Automation: SSMAutomationExecutionPreview | None = None
