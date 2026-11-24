from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubStringFilter(BaseModel):
    Value: StrictStr | None = None
    Comparison: StrictStr | None = None
