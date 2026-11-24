from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .memory_db_service_update_request import MemoryDBServiceUpdateRequest


class MemoryDBBatchUpdateClusterRequest(BaseModel):
    ClusterNames: list[StrictStr]
    ServiceUpdate: MemoryDBServiceUpdateRequest | None = None
