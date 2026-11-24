from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_user_profile_details import DataZoneUserProfileDetails


class DataZoneSubscribedUser(BaseModel):
    id: StrictStr | None = None
    details: DataZoneUserProfileDetails | None = None
