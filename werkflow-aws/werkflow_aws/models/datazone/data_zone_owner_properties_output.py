from __future__ import annotations
from pydantic import BaseModel
from .data_zone_owner_group_properties_output import DataZoneOwnerGroupPropertiesOutput
from .data_zone_owner_user_properties_output import DataZoneOwnerUserPropertiesOutput


class DataZoneOwnerPropertiesOutput(BaseModel):
    user: DataZoneOwnerUserPropertiesOutput | None = None
    group: DataZoneOwnerGroupPropertiesOutput | None = None
