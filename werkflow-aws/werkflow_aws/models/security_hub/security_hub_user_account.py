from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubUserAccount(BaseModel):
    Uid: StrictStr | None = None
    Name: StrictStr | None = None
