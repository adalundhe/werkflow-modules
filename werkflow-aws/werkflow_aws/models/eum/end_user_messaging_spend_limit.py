from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EndUserMessagingSpendLimit(BaseModel):
    Name: StrictStr | None = None
    EnforcedLimit: StrictInt | None = None
    MaxLimit: StrictInt | None = None
    Overridden: StrictBool | None = None
