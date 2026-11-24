from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ssm_automation_execution_filter import SSMAutomationExecutionFilter


class SSMDescribeAutomationExecutionsRequest(BaseModel):
    Filters: list[SSMAutomationExecutionFilter] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
