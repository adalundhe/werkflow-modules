from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .f_sx_create_open_zfs_origin_snapshot_configuration import FSxCreateOpenZFSOriginSnapshotConfiguration
from .f_sx_open_zfs_nfs_export import FSxOpenZFSNfsExport
from .f_sx_open_zfs_user_or_group_quota import FSxOpenZFSUserOrGroupQuota


class FSxCreateOpenZFSVolumeConfiguration(BaseModel):
    ParentVolumeId: StrictStr
    StorageCapacityReservationGiB: StrictInt | None = None
    StorageCapacityQuotaGiB: StrictInt | None = None
    RecordSizeKiB: StrictInt | None = None
    DataCompressionType: Literal['NONE', 'ZSTD', 'LZ4'] | None = None
    CopyTagsToSnapshots: StrictBool | None = None
    OriginSnapshot: FSxCreateOpenZFSOriginSnapshotConfiguration | None = None
    ReadOnly: StrictBool | None = None
    NfsExports: list[FSxOpenZFSNfsExport] | None = None
    UserAndGroupQuotas: list[FSxOpenZFSUserOrGroupQuota] | None = None
