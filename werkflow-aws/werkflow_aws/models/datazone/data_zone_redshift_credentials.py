from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_username_password import DataZoneUsernamePassword


class DataZoneRedshiftCredentials(BaseModel):
    secretArn: StrictStr | None = None
    usernamePassword: DataZoneUsernamePassword | None = None
