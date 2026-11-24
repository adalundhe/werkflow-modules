from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ssm_patch_orchestrator_filter import SSMPatchOrchestratorFilter


class SSMDescribeAvailablePatchesRequest(BaseModel):
    Filters: list[SSMPatchOrchestratorFilter] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
