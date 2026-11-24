from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lightsail_tag import LightsailTag


class LightsailCreateRelationalDatabaseSnapshotRequest(BaseModel):
    relationalDatabaseName: StrictStr
    relationalDatabaseSnapshotName: StrictStr
    tags: list[LightsailTag] | None = None
