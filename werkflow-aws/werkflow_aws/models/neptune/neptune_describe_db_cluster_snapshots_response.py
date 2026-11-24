from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .neptune_db_cluster_snapshot import NeptuneDBClusterSnapshot


class NeptuneDescribeDBClusterSnapshotsResponse(BaseModel):
    Marker: StrictStr | None = None
    DBClusterSnapshots: list[NeptuneDBClusterSnapshot] | None = None
    ResponseMetadata: dict[str, Any] | None = None
