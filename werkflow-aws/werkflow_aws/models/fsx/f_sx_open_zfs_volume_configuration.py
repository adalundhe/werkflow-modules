from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .f_sx_open_zfs_nfs_export import FSxOpenZFSNfsExport
from .f_sx_open_zfs_origin_snapshot_configuration import FSxOpenZFSOriginSnapshotConfiguration
from .f_sx_open_zfs_user_or_group_quota import FSxOpenZFSUserOrGroupQuota


class FSxOpenZFSVolumeConfiguration(BaseModel):
    ParentVolumeId: StrictStr | None = None
    VolumePath: StrictStr | None = None
    StorageCapacityReservationGiB: StrictInt | None = None
    StorageCapacityQuotaGiB: StrictInt | None = None
    RecordSizeKiB: StrictInt | None = None
    DataCompressionType: StrictStr | None = None
    CopyTagsToSnapshots: StrictBool | None = None
    OriginSnapshot: FSxOpenZFSOriginSnapshotConfiguration | None = None
    ReadOnly: StrictBool | None = None
    NfsExports: list[FSxOpenZFSNfsExport] | None = None
    UserAndGroupQuotas: list[FSxOpenZFSUserOrGroupQuota] | None = None
    RestoreToSnapshot: StrictStr | None = None
    DeleteIntermediateSnaphots: StrictBool | None = None
    DeleteClonedVolumes: StrictBool | None = None
    DeleteIntermediateData: StrictBool | None = None
    SourceSnapshotARN: StrictStr | None = None
    DestinationSnapshot: StrictStr | None = None
    CopyStrategy: StrictStr | None = None
