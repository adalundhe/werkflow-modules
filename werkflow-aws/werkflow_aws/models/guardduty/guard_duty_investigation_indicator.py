from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyInvestigationIndicator(BaseModel):
    Value: StrictStr | None = None
    Type: StrictStr | None = None
