from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MemoryDBUnprocessedCluster(BaseModel):
    ClusterName: StrictStr | None = None
    ErrorType: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
