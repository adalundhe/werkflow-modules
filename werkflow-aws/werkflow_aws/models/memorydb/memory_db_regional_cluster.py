from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MemoryDBRegionalCluster(BaseModel):
    ClusterName: StrictStr | None = None
    Region: StrictStr | None = None
    Status: StrictStr | None = None
    ARN: StrictStr | None = None
