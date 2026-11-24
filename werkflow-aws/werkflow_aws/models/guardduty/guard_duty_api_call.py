from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyApiCall(BaseModel):
    Operation: StrictStr | None = None
    Service: StrictStr | None = None
    Error: StrictStr | None = None
    UserAgent: StrictStr | None = None
