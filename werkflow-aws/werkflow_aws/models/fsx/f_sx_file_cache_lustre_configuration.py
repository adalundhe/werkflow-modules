from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .f_sx_file_cache_lustre_metadata_configuration import FSxFileCacheLustreMetadataConfiguration
from .f_sx_lustre_log_configuration import FSxLustreLogConfiguration


class FSxFileCacheLustreConfiguration(BaseModel):
    PerUnitStorageThroughput: StrictInt | None = None
    DeploymentType: StrictStr | None = None
    MountName: StrictStr | None = None
    WeeklyMaintenanceStartTime: StrictStr | None = None
    MetadataConfiguration: FSxFileCacheLustreMetadataConfiguration | None = None
    LogConfiguration: FSxLustreLogConfiguration | None = None
