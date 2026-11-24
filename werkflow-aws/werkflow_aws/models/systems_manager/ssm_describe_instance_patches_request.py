from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ssm_patch_orchestrator_filter import SSMPatchOrchestratorFilter


class SSMDescribeInstancePatchesRequest(BaseModel):
    InstanceId: StrictStr
    Filters: list[SSMPatchOrchestratorFilter] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
