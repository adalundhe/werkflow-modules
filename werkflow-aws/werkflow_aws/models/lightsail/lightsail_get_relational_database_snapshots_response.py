from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lightsail_relational_database_snapshot import LightsailRelationalDatabaseSnapshot


class LightsailGetRelationalDatabaseSnapshotsResponse(BaseModel):
    relationalDatabaseSnapshots: list[LightsailRelationalDatabaseSnapshot] | None = None
    nextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
