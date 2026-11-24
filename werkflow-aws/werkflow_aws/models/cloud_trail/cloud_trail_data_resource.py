from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailDataResource(BaseModel):
    Type: StrictStr | None = None
    Values: list[StrictStr] | None = None
