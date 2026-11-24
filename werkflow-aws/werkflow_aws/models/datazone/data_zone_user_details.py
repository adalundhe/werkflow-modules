from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneUserDetails(BaseModel):
    userId: StrictStr | None = None
