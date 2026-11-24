from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class DMSReloadTablesResponse(BaseModel):
    ReplicationTaskArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
