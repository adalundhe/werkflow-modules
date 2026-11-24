from __future__ import annotations
from pydantic import BaseModel
from .data_zone_iam_user_profile_details import DataZoneIamUserProfileDetails
from .data_zone_sso_user_profile_details import DataZoneSsoUserProfileDetails


class DataZoneUserProfileDetails(BaseModel):
    iam: DataZoneIamUserProfileDetails | None = None
    sso: DataZoneSsoUserProfileDetails | None = None
