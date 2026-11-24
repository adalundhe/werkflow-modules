from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftDeleteAuthenticationProfileRequest(BaseModel):
    AuthenticationProfileName: StrictStr
