from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SSMInventoryDeletionSummaryItem(BaseModel):
    Version: StrictStr | None = None
    Count: StrictInt | None = None
    RemainingCount: StrictInt | None = None
