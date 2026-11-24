from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DataZoneUpdateUserProfileRequest(BaseModel):
    domainIdentifier: StrictStr
    userIdentifier: StrictStr
    status: Literal['ASSIGNED', 'NOT_ASSIGNED', 'ACTIVATED', 'DEACTIVATED']
    type: Literal['IAM', 'SSO'] | None = None
    sessionName: StrictStr | None = None
