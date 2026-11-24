from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailStopRelationalDatabaseRequest(BaseModel):
    relationalDatabaseName: StrictStr
    relationalDatabaseSnapshotName: StrictStr | None = None
