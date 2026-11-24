from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneOwnerGroupPropertiesOutput(BaseModel):
    groupId: StrictStr | None = None
