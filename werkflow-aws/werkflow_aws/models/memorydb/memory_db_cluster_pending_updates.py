from __future__ import annotations
from pydantic import BaseModel
from .memory_dbac_ls_update_status import MemoryDBACLsUpdateStatus
from .memory_db_pending_modified_service_update import MemoryDBPendingModifiedServiceUpdate
from .memory_db_resharding_status import MemoryDBReshardingStatus


class MemoryDBClusterPendingUpdates(BaseModel):
    Resharding: MemoryDBReshardingStatus | None = None
    ACLs: MemoryDBACLsUpdateStatus | None = None
    ServiceUpdates: list[MemoryDBPendingModifiedServiceUpdate] | None = None
