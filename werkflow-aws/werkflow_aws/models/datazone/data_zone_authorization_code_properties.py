from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneAuthorizationCodeProperties(BaseModel):
    authorizationCode: StrictStr | None = None
    redirectUri: StrictStr | None = None
