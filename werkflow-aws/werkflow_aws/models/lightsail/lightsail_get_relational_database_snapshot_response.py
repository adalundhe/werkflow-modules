from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .lightsail_relational_database_snapshot import LightsailRelationalDatabaseSnapshot


class LightsailGetRelationalDatabaseSnapshotResponse(BaseModel):
    relationalDatabaseSnapshot: LightsailRelationalDatabaseSnapshot | None = None
    ResponseMetadata: dict[str, Any] | None = None
