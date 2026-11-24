from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRFailureDetails(BaseModel):
    Reason: StrictStr | None = None
    Message: StrictStr | None = None
    LogFile: StrictStr | None = None
