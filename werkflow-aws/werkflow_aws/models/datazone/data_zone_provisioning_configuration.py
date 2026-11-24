from __future__ import annotations
from pydantic import BaseModel
from .data_zone_lake_formation_configuration import DataZoneLakeFormationConfiguration


class DataZoneProvisioningConfiguration(BaseModel):
    lakeFormationConfiguration: DataZoneLakeFormationConfiguration | None = None
