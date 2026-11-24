from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .f_sx_lifecycle_transition_reason import FSxLifecycleTransitionReason
from .f_sx_snapmirror_destination import FSxSnapmirrorDestination
from .f_sx_snapmirror_exported_snapshot import FSxSnapmirrorExportedSnapshot
from .f_sx_snapmirror_relationship_policy import FSxSnapmirrorRelationshipPolicy
from .f_sx_snapmirror_source import FSxSnapmirrorSource
from .f_sx_snapmirror_transfer_state import FSxSnapmirrorTransferState
from .f_sx_tag import FSxTag


class FSxSnapmirrorRelationship(BaseModel):
    ResourceARN: StrictStr | None = None
    SnapmirrorRelationshipId: StrictStr | None = None
    FileSystemId: StrictStr | None = None
    Lifecycle: StrictStr | None = None
    LifecycleTransitionReason: FSxLifecycleTransitionReason | None = None
    Tags: list[FSxTag] | None = None
    Source: FSxSnapmirrorSource | None = None
    Destination: FSxSnapmirrorDestination | None = None
    SnapmirrorPolicy: FSxSnapmirrorRelationshipPolicy | None = None
    TransferSchedule: StrictStr | None = None
    ThrottleInKbps: StrictInt | None = None
    State: StrictStr | None = None
    Healthy: StrictBool | None = None
    UnhealthyReason: StrictStr | None = None
    LagTimeInMinutes: StrictInt | None = None
    ExportedSnapshot: FSxSnapmirrorExportedSnapshot | None = None
    TransferState: FSxSnapmirrorTransferState | None = None
    UUID: StrictStr | None = None
