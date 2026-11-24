from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DataZoneGetLineageNodeRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
    eventTimestamp: datetime.datetime | StrictStr | None = None
