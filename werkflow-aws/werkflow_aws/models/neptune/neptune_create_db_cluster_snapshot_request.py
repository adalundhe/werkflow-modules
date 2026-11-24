from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .neptune_tag import NeptuneTag


class NeptuneCreateDBClusterSnapshotRequest(BaseModel):
    DBClusterSnapshotIdentifier: StrictStr
    DBClusterIdentifier: StrictStr
    Tags: list[NeptuneTag] | None = None
