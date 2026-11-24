from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MemoryDBParameterGroup(BaseModel):
    Name: StrictStr | None = None
    Family: StrictStr | None = None
    Description: StrictStr | None = None
    ARN: StrictStr | None = None
