from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyContentPolicyFilter(BaseModel):
    Type: StrictStr | None = None
    Confidence: StrictStr | None = None
    Action: StrictStr | None = None
