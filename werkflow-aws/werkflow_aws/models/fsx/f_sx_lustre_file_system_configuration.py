from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .f_sx_data_repository_configuration import FSxDataRepositoryConfiguration
from .f_sx_file_system_lustre_metadata_configuration import FSxFileSystemLustreMetadataConfiguration
from .f_sx_lustre_log_configuration import FSxLustreLogConfiguration
from .f_sx_lustre_read_cache_configuration import FSxLustreReadCacheConfiguration
from .f_sx_lustre_root_squash_configuration import FSxLustreRootSquashConfiguration


class FSxLustreFileSystemConfiguration(BaseModel):
    WeeklyMaintenanceStartTime: StrictStr | None = None
    DataRepositoryConfiguration: FSxDataRepositoryConfiguration | None = None
    DeploymentType: StrictStr | None = None
    PerUnitStorageThroughput: StrictInt | None = None
    MountName: StrictStr | None = None
    DailyAutomaticBackupStartTime: StrictStr | None = None
    AutomaticBackupRetentionDays: StrictInt | None = None
    CopyTagsToBackups: StrictBool | None = None
    DriveCacheType: StrictStr | None = None
    DataCompressionType: StrictStr | None = None
    LogConfiguration: FSxLustreLogConfiguration | None = None
    RootSquashConfiguration: FSxLustreRootSquashConfiguration | None = None
    MetadataConfiguration: FSxFileSystemLustreMetadataConfiguration | None = None
    EfaEnabled: StrictBool | None = None
    ThroughputCapacity: StrictInt | None = None
    DataReadCacheConfiguration: FSxLustreReadCacheConfiguration | None = None
