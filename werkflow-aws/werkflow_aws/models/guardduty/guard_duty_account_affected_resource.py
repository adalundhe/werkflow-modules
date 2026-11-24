from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GuardDutyAccountAffectedResource(BaseModel):
    Identifier: StrictStr | None = None
    Type: StrictStr | None = None
    FindingCount: StrictInt | None = None
