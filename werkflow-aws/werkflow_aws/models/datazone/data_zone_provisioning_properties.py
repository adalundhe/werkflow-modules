from __future__ import annotations
from pydantic import BaseModel
from .data_zone_cloud_formation_properties import DataZoneCloudFormationProperties


class DataZoneProvisioningProperties(BaseModel):
    cloudFormation: DataZoneCloudFormationProperties | None = None
