from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DataZoneGetUserProfileRequest(BaseModel):
    domainIdentifier: StrictStr
    userIdentifier: StrictStr
    type: Literal['IAM', 'SSO'] | None = None
    sessionName: StrictStr | None = None
