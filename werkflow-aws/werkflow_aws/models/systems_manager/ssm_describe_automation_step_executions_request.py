from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ssm_step_execution_filter import SSMStepExecutionFilter


class SSMDescribeAutomationStepExecutionsRequest(BaseModel):
    AutomationExecutionId: StrictStr
    Filters: list[SSMStepExecutionFilter] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    ReverseOrder: StrictBool | None = None
