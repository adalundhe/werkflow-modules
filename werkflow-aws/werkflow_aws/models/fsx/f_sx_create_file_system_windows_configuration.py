from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .f_sx_disk_iops_configuration import FSxDiskIopsConfiguration
from .f_sx_self_managed_active_directory_configuration import FSxSelfManagedActiveDirectoryConfiguration
from .f_sx_windows_audit_log_create_configuration import FSxWindowsAuditLogCreateConfiguration
from .f_sx_windows_fsrm_configuration import FSxWindowsFsrmConfiguration


class FSxCreateFileSystemWindowsConfiguration(BaseModel):
    ThroughputCapacity: StrictInt
    ActiveDirectoryId: StrictStr | None = None
    SelfManagedActiveDirectoryConfiguration: FSxSelfManagedActiveDirectoryConfiguration | None = None
    DeploymentType: Literal['MULTI_AZ_1', 'SINGLE_AZ_1', 'SINGLE_AZ_2'] | None = None
    PreferredSubnetId: StrictStr | None = None
    WeeklyMaintenanceStartTime: StrictStr | None = None
    DailyAutomaticBackupStartTime: StrictStr | None = None
    AutomaticBackupRetentionDays: StrictInt | None = None
    CopyTagsToBackups: StrictBool | None = None
    Aliases: list[StrictStr] | None = None
    AuditLogConfiguration: FSxWindowsAuditLogCreateConfiguration | None = None
    DiskIopsConfiguration: FSxDiskIopsConfiguration | None = None
    FsrmConfiguration: FSxWindowsFsrmConfiguration | None = None
