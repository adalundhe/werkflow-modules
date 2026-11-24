from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightQuickSuiteActionsOption(BaseModel):
    AvailabilityStatus: StrictStr | None = None
