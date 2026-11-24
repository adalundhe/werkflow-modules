from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .directory_service_snapshot_limits import DirectoryServiceSnapshotLimits


class DirectoryServiceGetSnapshotLimitsResponse(BaseModel):
    SnapshotLimits: DirectoryServiceSnapshotLimits | None = None
    ResponseMetadata: dict[str, Any] | None = None
