from __future__ import annotations
import datetime
from typing import TYPE_CHECKING
from pydantic import BaseModel, StrictStr
from .f_sx_lifecycle_transition_reason import FSxLifecycleTransitionReason
from .f_sx_ontap_snapshot_configuration import FSxOntapSnapshotConfiguration
from .f_sx_tag import FSxTag

if TYPE_CHECKING:
    from .f_sx_administrative_action import FSxAdministrativeAction


class FSxSnapshot(BaseModel):
    ResourceARN: StrictStr | None = None
    SnapshotId: StrictStr | None = None
    Name: StrictStr | None = None
    VolumeId: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    Lifecycle: StrictStr | None = None
    SnapshotType: StrictStr | None = None
    LifecycleTransitionReason: FSxLifecycleTransitionReason | None = None
    Tags: list[FSxTag] | None = None
    AdministrativeActions: list[FSxAdministrativeAction] | None = None
    OntapConfiguration: FSxOntapSnapshotConfiguration | None = None
