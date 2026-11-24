from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .f_sx_disk_iops_configuration import FSxDiskIopsConfiguration
from .f_sx_open_zfs_read_cache_configuration import FSxOpenZFSReadCacheConfiguration


class FSxOpenZFSFileSystemConfiguration(BaseModel):
    AutomaticBackupRetentionDays: StrictInt | None = None
    CopyTagsToBackups: StrictBool | None = None
    CopyTagsToVolumes: StrictBool | None = None
    DailyAutomaticBackupStartTime: StrictStr | None = None
    DeploymentType: StrictStr | None = None
    ThroughputCapacity: StrictInt | None = None
    WeeklyMaintenanceStartTime: StrictStr | None = None
    DiskIopsConfiguration: FSxDiskIopsConfiguration | None = None
    RootVolumeId: StrictStr | None = None
    PreferredSubnetId: StrictStr | None = None
    EndpointIpAddressRange: StrictStr | None = None
    EndpointIpv6AddressRange: StrictStr | None = None
    RouteTableIds: list[StrictStr] | None = None
    EndpointIpAddress: StrictStr | None = None
    EndpointIpv6Address: StrictStr | None = None
    ReadCacheConfiguration: FSxOpenZFSReadCacheConfiguration | None = None
