from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class DevOpsGuruServiceResourceCost(BaseModel):
    Type: StrictStr | None = None
    State: StrictStr | None = None
    Count: StrictInt | None = None
    UnitCost: StrictFloat | StrictInt | None = None
    Cost: StrictFloat | StrictInt | None = None
