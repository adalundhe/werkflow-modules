from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .f_sx_aggregate_configuration import FSxAggregateConfiguration
from .f_sx_clone_configuration import FSxCloneConfiguration
from .f_sx_snaplock_configuration import FSxSnaplockConfiguration
from .f_sx_tiering_policy import FSxTieringPolicy


class FSxOntapVolumeConfiguration(BaseModel):
    FlexCacheEndpointType: StrictStr | None = None
    JunctionPath: StrictStr | None = None
    SecurityStyle: StrictStr | None = None
    SizeInMegabytes: StrictInt | None = None
    StorageEfficiencyEnabled: StrictBool | None = None
    StorageVirtualMachineId: StrictStr | None = None
    StorageVirtualMachineRoot: StrictBool | None = None
    TieringPolicy: FSxTieringPolicy | None = None
    UUID: StrictStr | None = None
    OntapVolumeType: StrictStr | None = None
    SnapshotPolicy: StrictStr | None = None
    CopyTagsToBackups: StrictBool | None = None
    SnaplockConfiguration: FSxSnaplockConfiguration | None = None
    VolumeStyle: StrictStr | None = None
    AggregateConfiguration: FSxAggregateConfiguration | None = None
    SizeInBytes: StrictInt | None = None
    CloneConfiguration: FSxCloneConfiguration | None = None
