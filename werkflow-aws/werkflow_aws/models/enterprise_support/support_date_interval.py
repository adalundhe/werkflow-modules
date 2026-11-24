from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SupportDateInterval(BaseModel):
    startDateTime: StrictStr | None = None
    endDateTime: StrictStr | None = None
