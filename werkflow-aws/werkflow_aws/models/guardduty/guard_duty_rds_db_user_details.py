from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyRdsDbUserDetails(BaseModel):
    User: StrictStr | None = None
    Application: StrictStr | None = None
    Database: StrictStr | None = None
    Ssl: StrictStr | None = None
    AuthMethod: StrictStr | None = None
