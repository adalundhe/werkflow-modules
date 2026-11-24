from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubDateRange(BaseModel):
    Value: StrictInt | None = None
    Unit: StrictStr | None = None
    Comparison: StrictStr | None = None
