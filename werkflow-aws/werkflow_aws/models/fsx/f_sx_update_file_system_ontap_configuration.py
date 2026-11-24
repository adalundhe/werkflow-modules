from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .f_sx_disk_iops_configuration import FSxDiskIopsConfiguration


class FSxUpdateFileSystemOntapConfiguration(BaseModel):
    AutomaticBackupRetentionDays: StrictInt | None = None
    DailyAutomaticBackupStartTime: StrictStr | None = None
    FsxAdminPassword: StrictStr | None = None
    WeeklyMaintenanceStartTime: StrictStr | None = None
    DiskIopsConfiguration: FSxDiskIopsConfiguration | None = None
    ThroughputCapacity: StrictInt | None = None
    AddRouteTableIds: list[StrictStr] | None = None
    RemoveRouteTableIds: list[StrictStr] | None = None
    ThroughputCapacityPerHAPair: StrictInt | None = None
    HAPairs: StrictInt | None = None
    EndpointIpv6AddressRange: StrictStr | None = None
