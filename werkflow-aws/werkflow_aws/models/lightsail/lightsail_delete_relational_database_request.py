from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class LightsailDeleteRelationalDatabaseRequest(BaseModel):
    relationalDatabaseName: StrictStr
    skipFinalSnapshot: StrictBool | None = None
    finalRelationalDatabaseSnapshotName: StrictStr | None = None
