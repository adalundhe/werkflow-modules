from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class MacieReplicationDetails(BaseModel):
    replicated: StrictBool | None = None
    replicatedExternally: StrictBool | None = None
    replicationAccounts: list[StrictStr] | None = None
