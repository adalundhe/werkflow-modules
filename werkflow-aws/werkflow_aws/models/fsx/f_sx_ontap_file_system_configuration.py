from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .f_sx_disk_iops_configuration import FSxDiskIopsConfiguration
from .f_sx_file_system_endpoints import FSxFileSystemEndpoints


class FSxOntapFileSystemConfiguration(BaseModel):
    AutomaticBackupRetentionDays: StrictInt | None = None
    DailyAutomaticBackupStartTime: StrictStr | None = None
    DeploymentType: StrictStr | None = None
    EndpointIpAddressRange: StrictStr | None = None
    Endpoints: FSxFileSystemEndpoints | None = None
    DiskIopsConfiguration: FSxDiskIopsConfiguration | None = None
    PreferredSubnetId: StrictStr | None = None
    RouteTableIds: list[StrictStr] | None = None
    ThroughputCapacity: StrictInt | None = None
    WeeklyMaintenanceStartTime: StrictStr | None = None
    FsxAdminPassword: StrictStr | None = None
    HAPairs: StrictInt | None = None
    ThroughputCapacityPerHAPair: StrictInt | None = None
    EndpointIpv6AddressRange: StrictStr | None = None
