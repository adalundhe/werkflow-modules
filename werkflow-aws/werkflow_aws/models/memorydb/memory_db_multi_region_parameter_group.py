from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MemoryDBMultiRegionParameterGroup(BaseModel):
    Name: StrictStr | None = None
    Family: StrictStr | None = None
    Description: StrictStr | None = None
    ARN: StrictStr | None = None
