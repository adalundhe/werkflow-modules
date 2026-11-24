from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .neptune_db_cluster import NeptuneDBCluster


class NeptuneRestoreDBClusterToPointInTimeResponse(BaseModel):
    DBCluster: NeptuneDBCluster | None = None
    ResponseMetadata: dict[str, Any] | None = None
