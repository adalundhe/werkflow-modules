from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class MacieApiCallDetails(BaseModel):
    api: StrictStr | None = None
    apiServiceName: StrictStr | None = None
    firstSeen: datetime.datetime | StrictStr | None = None
    lastSeen: datetime.datetime | StrictStr | None = None
