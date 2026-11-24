from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftModifyAuthenticationProfileRequest(BaseModel):
    AuthenticationProfileName: StrictStr
    AuthenticationProfileContent: StrictStr
