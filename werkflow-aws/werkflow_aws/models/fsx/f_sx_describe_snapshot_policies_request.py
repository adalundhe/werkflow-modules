from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .f_sx_snapshot_policy_filter import FSxSnapshotPolicyFilter


class FSxDescribeSnapshotPoliciesRequest(BaseModel):
    SnapshotPolicyIds: list[StrictStr] | None = None
    Filters: list[FSxSnapshotPolicyFilter] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
