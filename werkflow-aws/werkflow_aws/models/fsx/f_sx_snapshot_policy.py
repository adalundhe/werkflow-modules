from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .f_sx_lifecycle_transition_reason import FSxLifecycleTransitionReason
from .f_sx_snapshot_policy_schedule import FSxSnapshotPolicySchedule
from .f_sx_tag import FSxTag


class FSxSnapshotPolicy(BaseModel):
    ResourceARN: StrictStr | None = None
    SnapshotPolicyId: StrictStr | None = None
    FileSystemId: StrictStr | None = None
    StorageVirtualMachineId: StrictStr | None = None
    Name: StrictStr | None = None
    Enabled: StrictBool | None = None
    Schedules: list[FSxSnapshotPolicySchedule] | None = None
    Scope: StrictStr | None = None
    Lifecycle: StrictStr | None = None
    UUID: StrictStr | None = None
    LifecycleTransitionReason: FSxLifecycleTransitionReason | None = None
    Tags: list[FSxTag] | None = None
