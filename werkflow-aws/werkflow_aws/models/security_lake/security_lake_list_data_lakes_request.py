from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityLakeListDataLakesRequest(BaseModel):
    regions: list[StrictStr] | None = None
