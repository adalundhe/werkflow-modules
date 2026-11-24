from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubActorSession(BaseModel):
    Uid: StrictStr | None = None
    MfaStatus: StrictStr | None = None
    CreatedTime: StrictInt | None = None
    Issuer: StrictStr | None = None
