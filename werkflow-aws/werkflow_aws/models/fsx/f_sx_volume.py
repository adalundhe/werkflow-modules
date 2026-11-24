from __future__ import annotations
import datetime
from typing import TYPE_CHECKING
from pydantic import BaseModel, StrictStr
from .f_sx_lifecycle_transition_reason import FSxLifecycleTransitionReason
from .f_sx_ontap_volume_configuration import FSxOntapVolumeConfiguration
from .f_sx_open_zfs_volume_configuration import FSxOpenZFSVolumeConfiguration
from .f_sx_tag import FSxTag

if TYPE_CHECKING:
    from .f_sx_administrative_action import FSxAdministrativeAction


class FSxVolume(BaseModel):
    CreationTime: datetime.datetime | StrictStr | None = None
    FileSystemId: StrictStr | None = None
    Lifecycle: StrictStr | None = None
    Name: StrictStr | None = None
    OntapConfiguration: FSxOntapVolumeConfiguration | None = None
    ResourceARN: StrictStr | None = None
    Tags: list[FSxTag] | None = None
    VolumeId: StrictStr | None = None
    VolumeType: StrictStr | None = None
    LifecycleTransitionReason: FSxLifecycleTransitionReason | None = None
    AdministrativeActions: list[FSxAdministrativeAction] | None = None
    OpenZFSConfiguration: FSxOpenZFSVolumeConfiguration | None = None
