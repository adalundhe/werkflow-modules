from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectResourceReplicationStatus(BaseModel):
    Region: StrictStr | None = None
    Status: StrictStr | None = None
