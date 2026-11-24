from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudTrailDestination(BaseModel):
    Type: StrictStr | None = None
    Location: StrictStr | None = None
