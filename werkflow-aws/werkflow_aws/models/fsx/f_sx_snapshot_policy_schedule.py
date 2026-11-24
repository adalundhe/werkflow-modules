from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .f_sx_snapshot_policy_retention_period import FSxSnapshotPolicyRetentionPeriod


class FSxSnapshotPolicySchedule(BaseModel):
    Name: StrictStr | None = None
    Count: StrictInt | None = None
    Prefix: StrictStr | None = None
    SnapmirrorLabel: StrictStr | None = None
    RetentionPeriod: FSxSnapshotPolicyRetentionPeriod | None = None
