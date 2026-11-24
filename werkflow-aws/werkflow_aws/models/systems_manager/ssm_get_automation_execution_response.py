from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ssm_automation_execution import SSMAutomationExecution


class SSMGetAutomationExecutionResponse(BaseModel):
    AutomationExecution: SSMAutomationExecution | None = None
    ResponseMetadata: dict[str, Any] | None = None
