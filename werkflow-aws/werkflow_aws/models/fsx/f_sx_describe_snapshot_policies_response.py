from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .f_sx_snapshot_policy import FSxSnapshotPolicy


class FSxDescribeSnapshotPoliciesResponse(BaseModel):
    SnapshotPolicies: list[FSxSnapshotPolicy] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
