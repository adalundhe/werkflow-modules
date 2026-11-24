from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .f_sx_disk_iops_configuration import FSxDiskIopsConfiguration
from .f_sx_open_zfs_read_cache_configuration import FSxOpenZFSReadCacheConfiguration


class FSxUpdateFileSystemOpenZFSConfiguration(BaseModel):
    AutomaticBackupRetentionDays: StrictInt | None = None
    CopyTagsToBackups: StrictBool | None = None
    CopyTagsToVolumes: StrictBool | None = None
    DailyAutomaticBackupStartTime: StrictStr | None = None
    ThroughputCapacity: StrictInt | None = None
    WeeklyMaintenanceStartTime: StrictStr | None = None
    DiskIopsConfiguration: FSxDiskIopsConfiguration | None = None
    AddRouteTableIds: list[StrictStr] | None = None
    RemoveRouteTableIds: list[StrictStr] | None = None
    ReadCacheConfiguration: FSxOpenZFSReadCacheConfiguration | None = None
    EndpointIpv6AddressRange: StrictStr | None = None
