from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneLineageInfo(BaseModel):
    eventId: StrictStr | None = None
    eventStatus: StrictStr | None = None
    errorMessage: StrictStr | None = None
