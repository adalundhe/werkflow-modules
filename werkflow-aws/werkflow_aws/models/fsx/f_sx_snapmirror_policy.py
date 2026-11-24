from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .f_sx_lifecycle_transition_reason import FSxLifecycleTransitionReason
from .f_sx_snapmirror_policy_retention_rule import FSxSnapmirrorPolicyRetentionRule
from .f_sx_tag import FSxTag


class FSxSnapmirrorPolicy(BaseModel):
    ResourceARN: StrictStr | None = None
    SnapmirrorPolicyId: StrictStr | None = None
    FileSystemId: StrictStr | None = None
    StorageVirtualMachineId: StrictStr | None = None
    Name: StrictStr | None = None
    SnapshotCopyMode: StrictStr | None = None
    RetentionRules: list[FSxSnapmirrorPolicyRetentionRule] | None = None
    TransferSchedule: StrictStr | None = None
    NetworkCompressionEnabled: StrictBool | None = None
    ThrottleInKbps: StrictInt | None = None
    Scope: StrictStr | None = None
    Lifecycle: StrictStr | None = None
    UUID: StrictStr | None = None
    LifecycleTransitionReason: FSxLifecycleTransitionReason | None = None
    Tags: list[FSxTag] | None = None
