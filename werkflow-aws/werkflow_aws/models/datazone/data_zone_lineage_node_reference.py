from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DataZoneLineageNodeReference(BaseModel):
    id: StrictStr | None = None
    eventTimestamp: datetime.datetime | StrictStr | None = None
