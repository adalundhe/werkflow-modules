from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailGetRelationalDatabaseSnapshotsRequest(BaseModel):
    pageToken: StrictStr | None = None
