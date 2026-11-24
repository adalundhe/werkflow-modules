from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .f_sx_tiering_policy import FSxTieringPolicy
from .f_sx_update_clone_configuration import FSxUpdateCloneConfiguration
from .f_sx_update_snaplock_configuration import FSxUpdateSnaplockConfiguration


class FSxUpdateOntapVolumeConfiguration(BaseModel):
    JunctionPath: StrictStr | None = None
    SecurityStyle: Literal['UNIX', 'NTFS', 'MIXED'] | None = None
    SizeInMegabytes: StrictInt | None = None
    StorageEfficiencyEnabled: StrictBool | None = None
    TieringPolicy: FSxTieringPolicy | None = None
    SnapshotPolicy: StrictStr | None = None
    CopyTagsToBackups: StrictBool | None = None
    SnaplockConfiguration: FSxUpdateSnaplockConfiguration | None = None
    SizeInBytes: StrictInt | None = None
    CloneConfiguration: FSxUpdateCloneConfiguration | None = None
