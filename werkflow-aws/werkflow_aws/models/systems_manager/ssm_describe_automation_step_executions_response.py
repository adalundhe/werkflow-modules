from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_step_execution import SSMStepExecution


class SSMDescribeAutomationStepExecutionsResponse(BaseModel):
    StepExecutions: list[SSMStepExecution] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
