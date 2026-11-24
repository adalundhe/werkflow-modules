from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubSecurityControlParameter(BaseModel):
    Name: StrictStr | None = None
    Value: list[StrictStr] | None = None
