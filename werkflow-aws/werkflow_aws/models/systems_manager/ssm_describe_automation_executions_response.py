from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_automation_execution_metadata import SSMAutomationExecutionMetadata


class SSMDescribeAutomationExecutionsResponse(BaseModel):
    AutomationExecutionMetadataList: list[SSMAutomationExecutionMetadata] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
