from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailContextKeySelector(BaseModel):
    Type: StrictStr | None = None
    Equals: list[StrictStr] | None = None
