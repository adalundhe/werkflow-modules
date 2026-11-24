from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .f_sx_file_cache_lustre_metadata_configuration import FSxFileCacheLustreMetadataConfiguration


class FSxCreateFileCacheLustreConfiguration(BaseModel):
    PerUnitStorageThroughput: StrictInt
    DeploymentType: Literal['CACHE_1']
    MetadataConfiguration: FSxFileCacheLustreMetadataConfiguration
    WeeklyMaintenanceStartTime: StrictStr | None = None
