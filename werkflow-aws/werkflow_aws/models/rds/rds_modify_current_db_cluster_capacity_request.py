from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class RDSModifyCurrentDBClusterCapacityRequest(BaseModel):
    DBClusterIdentifier: StrictStr
    Capacity: StrictInt | None = None
    SecondsBeforeTimeout: StrictInt | None = None
    TimeoutAction: StrictStr | None = None
