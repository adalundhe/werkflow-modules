from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .f_sx_disk_iops_configuration import FSxDiskIopsConfiguration


class FSxCreateFileSystemOntapConfiguration(BaseModel):
    DeploymentType: Literal['MULTI_AZ_1', 'SINGLE_AZ_1', 'SINGLE_AZ_2', 'MULTI_AZ_2', 'SINGLE_AZ_3', 'MULTI_AZ_3']
    AutomaticBackupRetentionDays: StrictInt | None = None
    DailyAutomaticBackupStartTime: StrictStr | None = None
    EndpointIpAddressRange: StrictStr | None = None
    FsxAdminPassword: StrictStr | None = None
    DiskIopsConfiguration: FSxDiskIopsConfiguration | None = None
    PreferredSubnetId: StrictStr | None = None
    RouteTableIds: list[StrictStr] | None = None
    ThroughputCapacity: StrictInt | None = None
    WeeklyMaintenanceStartTime: StrictStr | None = None
    HAPairs: StrictInt | None = None
    ThroughputCapacityPerHAPair: StrictInt | None = None
    EndpointIpv6AddressRange: StrictStr | None = None
