from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftCreateAuthenticationProfileRequest(BaseModel):
    AuthenticationProfileName: StrictStr
    AuthenticationProfileContent: StrictStr
