from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt
from .f_sx_open_zfs_nfs_export import FSxOpenZFSNfsExport
from .f_sx_open_zfs_user_or_group_quota import FSxOpenZFSUserOrGroupQuota


class FSxUpdateOpenZFSVolumeConfiguration(BaseModel):
    StorageCapacityReservationGiB: StrictInt | None = None
    StorageCapacityQuotaGiB: StrictInt | None = None
    RecordSizeKiB: StrictInt | None = None
    DataCompressionType: Literal['NONE', 'ZSTD', 'LZ4'] | None = None
    NfsExports: list[FSxOpenZFSNfsExport] | None = None
    UserAndGroupQuotas: list[FSxOpenZFSUserOrGroupQuota] | None = None
    ReadOnly: StrictBool | None = None
