from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class MSKUpdateReplicationInfoResponse(BaseModel):
    ReplicatorArn: StrictStr | None = None
    ReplicatorState: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
