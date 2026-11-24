from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubGroupByValue(BaseModel):
    FieldValue: StrictStr | None = None
    Count: StrictInt | None = None
