from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .f_sx_snapmirror_policy_retention_rule import FSxSnapmirrorPolicyRetentionRule
from .f_sx_tag import FSxTag


class FSxCreateSnapmirrorPolicyRequest(BaseModel):
    Name: StrictStr
    ClientRequestToken: StrictStr | None = None
    FileSystemId: StrictStr | None = None
    StorageVirtualMachineId: StrictStr | None = None
    SnapshotCopyMode: Literal['COPY_ALL_SOURCE_SNAPSHOTS', 'COPY_LATEST_SOURCE_SNAPSHOT', 'NO_CREATE_SNAPSHOT_ON_SOURCE'] | None = None
    RetentionRules: list[FSxSnapmirrorPolicyRetentionRule] | None = None
    TransferSchedule: StrictStr | None = None
    NetworkCompressionEnabled: StrictBool | None = None
    ThrottleInKbps: StrictInt | None = None
    Tags: list[FSxTag] | None = None
