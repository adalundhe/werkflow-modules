from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .f_sx_alias import FSxAlias
from .f_sx_disk_iops_configuration import FSxDiskIopsConfiguration
from .f_sx_self_managed_active_directory_attributes import FSxSelfManagedActiveDirectoryAttributes
from .f_sx_windows_audit_log_configuration import FSxWindowsAuditLogConfiguration
from .f_sx_windows_fsrm_configuration import FSxWindowsFsrmConfiguration


class FSxWindowsFileSystemConfiguration(BaseModel):
    ActiveDirectoryId: StrictStr | None = None
    SelfManagedActiveDirectoryConfiguration: FSxSelfManagedActiveDirectoryAttributes | None = None
    DeploymentType: StrictStr | None = None
    RemoteAdministrationEndpoint: StrictStr | None = None
    PreferredSubnetId: StrictStr | None = None
    PreferredFileServerIp: StrictStr | None = None
    ThroughputCapacity: StrictInt | None = None
    MaintenanceOperationsInProgress: list[StrictStr] | None = None
    WeeklyMaintenanceStartTime: StrictStr | None = None
    DailyAutomaticBackupStartTime: StrictStr | None = None
    AutomaticBackupRetentionDays: StrictInt | None = None
    CopyTagsToBackups: StrictBool | None = None
    Aliases: list[FSxAlias] | None = None
    AuditLogConfiguration: FSxWindowsAuditLogConfiguration | None = None
    DiskIopsConfiguration: FSxDiskIopsConfiguration | None = None
    PreferredFileServerIpv6: StrictStr | None = None
    FsrmConfiguration: FSxWindowsFsrmConfiguration | None = None
