from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .f_sx_disk_iops_configuration import FSxDiskIopsConfiguration
from .f_sx_self_managed_active_directory_configuration_updates import FSxSelfManagedActiveDirectoryConfigurationUpdates
from .f_sx_windows_audit_log_create_configuration import FSxWindowsAuditLogCreateConfiguration
from .f_sx_windows_fsrm_configuration import FSxWindowsFsrmConfiguration


class FSxUpdateFileSystemWindowsConfiguration(BaseModel):
    WeeklyMaintenanceStartTime: StrictStr | None = None
    DailyAutomaticBackupStartTime: StrictStr | None = None
    AutomaticBackupRetentionDays: StrictInt | None = None
    ThroughputCapacity: StrictInt | None = None
    SelfManagedActiveDirectoryConfiguration: FSxSelfManagedActiveDirectoryConfigurationUpdates | None = None
    AuditLogConfiguration: FSxWindowsAuditLogCreateConfiguration | None = None
    DiskIopsConfiguration: FSxDiskIopsConfiguration | None = None
    FsrmConfiguration: FSxWindowsFsrmConfiguration | None = None
