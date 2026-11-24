from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_user_profile_details import DataZoneUserProfileDetails


class DataZoneUserProfileSummary(BaseModel):
    domainId: StrictStr | None = None
    id: StrictStr | None = None
    type: StrictStr | None = None
    status: StrictStr | None = None
    details: DataZoneUserProfileDetails | None = None
