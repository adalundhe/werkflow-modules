from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .f_sx_create_aggregate_configuration import FSxCreateAggregateConfiguration
from .f_sx_create_clone_configuration import FSxCreateCloneConfiguration
from .f_sx_create_snaplock_configuration import FSxCreateSnaplockConfiguration
from .f_sx_tiering_policy import FSxTieringPolicy


class FSxCreateOntapVolumeConfiguration(BaseModel):
    StorageVirtualMachineId: StrictStr
    JunctionPath: StrictStr | None = None
    SecurityStyle: Literal['UNIX', 'NTFS', 'MIXED'] | None = None
    SizeInMegabytes: StrictInt | None = None
    StorageEfficiencyEnabled: StrictBool | None = None
    TieringPolicy: FSxTieringPolicy | None = None
    OntapVolumeType: Literal['RW', 'DP'] | None = None
    SnapshotPolicy: StrictStr | None = None
    CopyTagsToBackups: StrictBool | None = None
    SnaplockConfiguration: FSxCreateSnaplockConfiguration | None = None
    VolumeStyle: Literal['FLEXVOL', 'FLEXGROUP'] | None = None
    AggregateConfiguration: FSxCreateAggregateConfiguration | None = None
    SizeInBytes: StrictInt | None = None
    CloneConfiguration: FSxCreateCloneConfiguration | None = None
