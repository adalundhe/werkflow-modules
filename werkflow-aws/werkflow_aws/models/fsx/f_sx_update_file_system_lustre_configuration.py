from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .f_sx_lustre_log_create_configuration import FSxLustreLogCreateConfiguration
from .f_sx_lustre_read_cache_configuration import FSxLustreReadCacheConfiguration
from .f_sx_lustre_root_squash_configuration import FSxLustreRootSquashConfiguration
from .f_sx_update_file_system_lustre_metadata_configuration import FSxUpdateFileSystemLustreMetadataConfiguration


class FSxUpdateFileSystemLustreConfiguration(BaseModel):
    WeeklyMaintenanceStartTime: StrictStr | None = None
    DailyAutomaticBackupStartTime: StrictStr | None = None
    AutomaticBackupRetentionDays: StrictInt | None = None
    AutoImportPolicy: Literal['NONE', 'NEW', 'NEW_CHANGED', 'NEW_CHANGED_DELETED'] | None = None
    DataCompressionType: Literal['NONE', 'LZ4'] | None = None
    LogConfiguration: FSxLustreLogCreateConfiguration | None = None
    RootSquashConfiguration: FSxLustreRootSquashConfiguration | None = None
    PerUnitStorageThroughput: StrictInt | None = None
    MetadataConfiguration: FSxUpdateFileSystemLustreMetadataConfiguration | None = None
    ThroughputCapacity: StrictInt | None = None
    DataReadCacheConfiguration: FSxLustreReadCacheConfiguration | None = None
