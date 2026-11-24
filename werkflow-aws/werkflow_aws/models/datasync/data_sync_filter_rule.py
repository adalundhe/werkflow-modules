from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataSyncFilterRule(BaseModel):
    FilterType: StrictStr | None = None
    Value: StrictStr | None = None
