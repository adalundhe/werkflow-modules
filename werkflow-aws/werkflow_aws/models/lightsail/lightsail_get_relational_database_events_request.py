from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LightsailGetRelationalDatabaseEventsRequest(BaseModel):
    relationalDatabaseName: StrictStr
    durationInMinutes: StrictInt | None = None
    pageToken: StrictStr | None = None
