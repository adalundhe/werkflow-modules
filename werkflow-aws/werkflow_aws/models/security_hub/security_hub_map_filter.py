from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubMapFilter(BaseModel):
    Key: StrictStr | None = None
    Value: StrictStr | None = None
    Comparison: StrictStr | None = None
