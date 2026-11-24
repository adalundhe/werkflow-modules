from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneBasicAuthenticationCredentials(BaseModel):
    userName: StrictStr | None = None
    password: StrictStr | None = None
