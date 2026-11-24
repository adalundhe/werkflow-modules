from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class GuardDutySession(BaseModel):
    Uid: StrictStr | None = None
    MfaStatus: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    Issuer: StrictStr | None = None
