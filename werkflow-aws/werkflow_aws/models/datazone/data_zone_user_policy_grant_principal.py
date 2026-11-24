from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_all_users_grant_filter import DataZoneAllUsersGrantFilter


class DataZoneUserPolicyGrantPrincipal(BaseModel):
    userIdentifier: StrictStr | None = None
    allUsersGrantFilter: DataZoneAllUsersGrantFilter | None = None
