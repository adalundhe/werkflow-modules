from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .config_service_remediation_execution_status import ConfigServiceRemediationExecutionStatus


class ConfigServiceDescribeRemediationExecutionStatusResponse(BaseModel):
    RemediationExecutionStatuses: list[ConfigServiceRemediationExecutionStatus] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
