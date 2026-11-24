from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .f_sx_snapshot_policy_schedule import FSxSnapshotPolicySchedule
from .f_sx_tag import FSxTag


class FSxCreateSnapshotPolicyRequest(BaseModel):
    Name: StrictStr
    Schedules: list[FSxSnapshotPolicySchedule]
    ClientRequestToken: StrictStr | None = None
    FileSystemId: StrictStr | None = None
    StorageVirtualMachineId: StrictStr | None = None
    Enabled: StrictBool | None = None
    Tags: list[FSxTag] | None = None
