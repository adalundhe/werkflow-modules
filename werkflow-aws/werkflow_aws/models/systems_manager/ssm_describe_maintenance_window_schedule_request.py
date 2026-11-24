from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .ssm_patch_orchestrator_filter import SSMPatchOrchestratorFilter
from .ssm_target import SSMTarget


class SSMDescribeMaintenanceWindowScheduleRequest(BaseModel):
    WindowId: StrictStr | None = None
    Targets: list[SSMTarget] | None = None
    ResourceType: Literal['INSTANCE', 'RESOURCE_GROUP'] | None = None
    Filters: list[SSMPatchOrchestratorFilter] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
