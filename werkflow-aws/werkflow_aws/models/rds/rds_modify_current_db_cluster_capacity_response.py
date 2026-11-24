from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class RDSModifyCurrentDBClusterCapacityResponse(BaseModel):
    DBClusterIdentifier: StrictStr | None = None
    PendingCapacity: StrictInt | None = None
    CurrentCapacity: StrictInt | None = None
    SecondsBeforeTimeout: StrictInt | None = None
    TimeoutAction: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
