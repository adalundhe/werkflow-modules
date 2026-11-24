from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .f_sx_disk_iops_configuration import FSxDiskIopsConfiguration
from .f_sx_open_zfs_create_root_volume_configuration import FSxOpenZFSCreateRootVolumeConfiguration
from .f_sx_open_zfs_read_cache_configuration import FSxOpenZFSReadCacheConfiguration


class FSxCreateFileSystemOpenZFSConfiguration(BaseModel):
    DeploymentType: Literal['SINGLE_AZ_1', 'SINGLE_AZ_2', 'SINGLE_AZ_HA_1', 'SINGLE_AZ_HA_2', 'MULTI_AZ_1']
    ThroughputCapacity: StrictInt
    AutomaticBackupRetentionDays: StrictInt | None = None
    CopyTagsToBackups: StrictBool | None = None
    CopyTagsToVolumes: StrictBool | None = None
    DailyAutomaticBackupStartTime: StrictStr | None = None
    WeeklyMaintenanceStartTime: StrictStr | None = None
    DiskIopsConfiguration: FSxDiskIopsConfiguration | None = None
    RootVolumeConfiguration: FSxOpenZFSCreateRootVolumeConfiguration | None = None
    PreferredSubnetId: StrictStr | None = None
    EndpointIpAddressRange: StrictStr | None = None
    EndpointIpv6AddressRange: StrictStr | None = None
    RouteTableIds: list[StrictStr] | None = None
    ReadCacheConfiguration: FSxOpenZFSReadCacheConfiguration | None = None
