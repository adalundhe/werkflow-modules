from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .f_sx_create_file_system_lustre_metadata_configuration import FSxCreateFileSystemLustreMetadataConfiguration
from .f_sx_lustre_log_create_configuration import FSxLustreLogCreateConfiguration
from .f_sx_lustre_read_cache_configuration import FSxLustreReadCacheConfiguration
from .f_sx_lustre_root_squash_configuration import FSxLustreRootSquashConfiguration


class FSxCreateFileSystemLustreConfiguration(BaseModel):
    WeeklyMaintenanceStartTime: StrictStr | None = None
    ImportPath: StrictStr | None = None
    ExportPath: StrictStr | None = None
    ImportedFileChunkSize: StrictInt | None = None
    DeploymentType: Literal['SCRATCH_1', 'SCRATCH_2', 'PERSISTENT_1', 'PERSISTENT_2'] | None = None
    AutoImportPolicy: Literal['NONE', 'NEW', 'NEW_CHANGED', 'NEW_CHANGED_DELETED'] | None = None
    PerUnitStorageThroughput: StrictInt | None = None
    DailyAutomaticBackupStartTime: StrictStr | None = None
    AutomaticBackupRetentionDays: StrictInt | None = None
    CopyTagsToBackups: StrictBool | None = None
    DriveCacheType: Literal['NONE', 'READ'] | None = None
    DataCompressionType: Literal['NONE', 'LZ4'] | None = None
    EfaEnabled: StrictBool | None = None
    LogConfiguration: FSxLustreLogCreateConfiguration | None = None
    RootSquashConfiguration: FSxLustreRootSquashConfiguration | None = None
    MetadataConfiguration: FSxCreateFileSystemLustreMetadataConfiguration | None = None
    ThroughputCapacity: StrictInt | None = None
    DataReadCacheConfiguration: FSxLustreReadCacheConfiguration | None = None
