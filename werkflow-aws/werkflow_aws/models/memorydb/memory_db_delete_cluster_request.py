from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MemoryDBDeleteClusterRequest(BaseModel):
    ClusterName: StrictStr
    MultiRegionClusterName: StrictStr | None = None
    FinalSnapshotName: StrictStr | None = None
