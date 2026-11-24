from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GuardDutyResourceDistribution(BaseModel):
    ResourceType: StrictStr | None = None
    Identifier: StrictStr | None = None
    Count: StrictInt | None = None
