from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneGroupDetails(BaseModel):
    groupId: StrictStr | None = None
