from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneGlueOAuth2Credentials(BaseModel):
    userManagedClientApplicationClientSecret: StrictStr | None = None
    accessToken: StrictStr | None = None
    refreshToken: StrictStr | None = None
    jwtToken: StrictStr | None = None
