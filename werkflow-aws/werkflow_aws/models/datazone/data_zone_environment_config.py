from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_package_config import DataZonePackageConfig


class DataZoneEnvironmentConfig(BaseModel):
    imageVersion: StrictStr | None = None
    packageConfig: DataZonePackageConfig | None = None
