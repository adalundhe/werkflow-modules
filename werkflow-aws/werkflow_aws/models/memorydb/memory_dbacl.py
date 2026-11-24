from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .memory_dbacl_pending_changes import MemoryDBACLPendingChanges


class MemoryDBACL(BaseModel):
    Name: StrictStr | None = None
    Status: StrictStr | None = None
    UserNames: list[StrictStr] | None = None
    MinimumEngineVersion: StrictStr | None = None
    PendingChanges: MemoryDBACLPendingChanges | None = None
    Clusters: list[StrictStr] | None = None
    ARN: StrictStr | None = None
