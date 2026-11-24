from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_maintenance_window_execution_task_invocation_identity import SSMMaintenanceWindowExecutionTaskInvocationIdentity


class SSMDescribeMaintenanceWindowExecutionTaskInvocationsResponse(BaseModel):
    WindowExecutionTaskInvocationIdentities: list[SSMMaintenanceWindowExecutionTaskInvocationIdentity] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
