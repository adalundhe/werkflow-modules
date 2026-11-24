from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class GuardDutySignalGroup(BaseModel):
    FindingType: StrictStr | None = None
    Severity: StrictFloat | StrictInt | None = None
    Count: StrictInt | None = None
