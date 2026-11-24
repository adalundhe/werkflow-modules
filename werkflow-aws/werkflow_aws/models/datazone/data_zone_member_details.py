from __future__ import annotations
from pydantic import BaseModel
from .data_zone_group_details import DataZoneGroupDetails
from .data_zone_user_details import DataZoneUserDetails


class DataZoneMemberDetails(BaseModel):
    user: DataZoneUserDetails | None = None
    group: DataZoneGroupDetails | None = None
