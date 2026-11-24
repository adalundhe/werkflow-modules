from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DataZoneCreateUserProfileRequest(BaseModel):
    domainIdentifier: StrictStr
    userIdentifier: StrictStr
    userType: Literal['IAM_USER', 'IAM_ROLE', 'SSO_USER', 'IAM_ROLE_SESSION'] | None = None
    sessionName: StrictStr | None = None
    clientToken: StrictStr | None = None
