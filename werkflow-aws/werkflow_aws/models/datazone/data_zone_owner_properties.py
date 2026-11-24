from __future__ import annotations
from pydantic import BaseModel
from .data_zone_owner_group_properties import DataZoneOwnerGroupProperties
from .data_zone_owner_user_properties import DataZoneOwnerUserProperties


class DataZoneOwnerProperties(BaseModel):
    user: DataZoneOwnerUserProperties | None = None
    group: DataZoneOwnerGroupProperties | None = None
