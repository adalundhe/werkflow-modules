from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftAuthenticationProfile(BaseModel):
    AuthenticationProfileName: StrictStr | None = None
    AuthenticationProfileContent: StrictStr | None = None
